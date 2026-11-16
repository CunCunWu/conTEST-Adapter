#!/usr/bin/env python3
"""Extract the article body from the installed conTEST Adapter DocFX site.

The script uses only Python's standard library.  It intentionally drops the
DocFX navigation and theme so the generated Markdown remains searchable and
compact.  Run it from the repository root; see docs/source-and-version.md.
"""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_SOURCE = Path(
    r"C:\Program Files\conTEST 1.15\Documentation\ContinuousTesting Adapter"
)


class ArticleExtractor(HTMLParser):
    """Capture the inner HTML of the first article element."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "article" and self.depth == 0:
            self.depth = 1
            return
        if self.depth:
            self.depth += 1
            attrs_text = "".join(
                f' {key}="{html.escape(value or "", quote=True)}"'
                for key, value in attrs
            )
            self.parts.append(f"<{tag}{attrs_text}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.depth:
            attrs_text = "".join(
                f' {key}="{html.escape(value or "", quote=True)}"'
                for key, value in attrs
            )
            self.parts.append(f"<{tag}{attrs_text} />")

    def handle_endtag(self, tag: str) -> None:
        if not self.depth:
            return
        self.depth -= 1
        if self.depth:
            self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.depth:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self.depth:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self.depth:
            self.parts.append(f"&#{name};")


def clean_inline(fragment: str) -> str:
    fragment = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>", r"**\1**", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<(?:em|i)\b[^>]*>(.*?)</(?:em|i)>", r"*\1*", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<code\b[^>]*>(.*?)</code>", r"`\1`", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<br\s*/?>", "<br>", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = fragment.replace("\xa0", " ")
    fragment = re.sub(r"[ \t\r\f\v]+", " ", fragment)
    fragment = re.sub(r" *\n *", " ", fragment)
    return fragment.strip()


def table_to_markdown(table_html: str) -> str:
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", table_html, flags=re.I | re.S)
    matrix: list[list[str]] = []
    for row in rows:
        cells = re.findall(r"<(?:th|td)\b[^>]*>(.*?)</(?:th|td)>", row, flags=re.I | re.S)
        if cells:
            matrix.append([clean_inline(cell).replace("|", "\\|") for cell in cells])
    if not matrix:
        return ""
    width = max(len(row) for row in matrix)
    matrix = [row + [""] * (width - len(row)) for row in matrix]
    header = matrix[0]
    body = matrix[1:]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def article_to_markdown(source: Path) -> str:
    parser = ArticleExtractor()
    parser.feed(source.read_text(encoding="utf-8"))
    body = "".join(parser.parts)
    if not body.strip():
        raise ValueError(f"No article body found in {source}")

    placeholders: dict[str, str] = {}

    def hold(value: str) -> str:
        key = f"@@BLOCK{len(placeholders)}@@"
        placeholders[key] = value
        return f"\n\n{key}\n\n"

    body = re.sub(
        r"<pre\b[^>]*>\s*<code\b[^>]*>(.*?)</code>\s*</pre>",
        lambda m: hold("```text\n" + html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() + "\n```"),
        body,
        flags=re.I | re.S,
    )
    body = re.sub(
        r"<table\b[^>]*>(.*?)</table>",
        lambda m: hold(table_to_markdown(m.group(1))),
        body,
        flags=re.I | re.S,
    )
    body = re.sub(r"<h([1-6])\b[^>]*>(.*?)</h\1>", lambda m: f"\n\n{'#' * int(m.group(1))} {clean_inline(m.group(2))}\n\n", body, flags=re.I | re.S)
    body = re.sub(r"<li\b[^>]*>(.*?)</li>", lambda m: f"\n- {clean_inline(m.group(1))}", body, flags=re.I | re.S)
    body = re.sub(r"<p\b[^>]*>(.*?)</p>", lambda m: f"\n\n{clean_inline(m.group(1))}\n\n", body, flags=re.I | re.S)
    body = body.replace("<br>", "  \n")
    body = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", body, flags=re.I | re.S)
    body = re.sub(r"<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>", r"**\1**", body, flags=re.I | re.S)
    body = re.sub(r"<(?:em|i)\b[^>]*>(.*?)</(?:em|i)>", r"*\1*", body, flags=re.I | re.S)
    body = re.sub(r"<code\b[^>]*>(.*?)</code>", r"`\1`", body, flags=re.I | re.S)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body).replace("\xa0", " ")
    body = "\n".join(re.sub(r"[ \t\r\f\v]+", " ", line).strip() for line in body.splitlines())
    for key, value in placeholders.items():
        body = body.replace(key, value)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    body = "\n".join(line.rstrip() for line in body.splitlines()).rstrip() + "\n"
    return body


def main() -> None:
    argp = argparse.ArgumentParser()
    argp.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    argp.add_argument("--output", type=Path, default=Path("reference"))
    args = argp.parse_args()

    adapters = ["general", "GrpcAdapter", "TcpIpAdapter", "SerialAdapter", "MQTTAdapter", "DIOAdapter"]
    generated = 0
    for adapter in adapters:
        source_dir = args.source / adapter
        if not source_dir.is_dir():
            raise FileNotFoundError(source_dir)
        output_dir = args.output / adapter
        output_dir.mkdir(parents=True, exist_ok=True)
        for source in sorted(source_dir.glob("*.html")):
            markdown = article_to_markdown(source)
            banner = (
                "> Extracted from the locally installed conTEST 1.15 Adapter help. "
                "See [source policy](../../docs/source-and-version.md).\n\n"
            )
            (output_dir / f"{source.stem}.md").write_text(banner + markdown, encoding="utf-8", newline="\n")
            generated += 1
    grpc_integration = (args.output / "GrpcAdapter" / "integration.md").read_text(encoding="utf-8")
    proto_match = re.search(r"```text\n(syntax = \"proto3\";.*)\n```", grpc_integration, flags=re.S)
    if not proto_match:
        raise ValueError("Could not locate CtGrpcRemote.proto in gRPC integration page")
    proto_output = Path("protocol/grpc/CtGrpcRemote.proto")
    proto_output.parent.mkdir(parents=True, exist_ok=True)
    proto_output.write_text(proto_match.group(1).strip() + "\n", encoding="utf-8", newline="\n")
    print(f"Generated {generated} Markdown reference pages in {args.output}")


if __name__ == "__main__":
    main()
