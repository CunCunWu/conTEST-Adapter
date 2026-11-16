#!/usr/bin/env python3
"""Offline consistency checks for the conTEST Adapter guide."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


def check_links() -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for page in ROOT.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-z]+://", target, flags=re.I):
                continue
            target = unquote(target.strip("<>"))
            resolved = (page.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken link: {page.relative_to(ROOT)} -> {raw_target}")
    return errors


def check_contract() -> list[str]:
    errors: list[str] = []
    proto = ROOT / "protocol/grpc/CtGrpcRemote.proto"
    if not proto.is_file():
        return ["missing protocol/grpc/CtGrpcRemote.proto"]
    proto_text = proto.read_text(encoding="utf-8")
    for service in (
        "CtGrpcAdapter",
        "PostProcessingService",
        "ConditionMonitoringService",
        "LiveMonitoringService",
    ):
        if f"service {service}" not in proto_text:
            errors.append(f"missing gRPC service: {service}")

    reference_pages = list((ROOT / "reference").glob("*/*.md"))
    if len(reference_pages) != 99:
        errors.append(f"expected 99 reference pages, found {len(reference_pages)}")

    tcp_start = (1).to_bytes(4, "little") + b"Start"
    serial_start = tcp_start + b"*"
    if tcp_start.hex() != "010000005374617274":
        errors.append("TCP Start frame invariant failed")
    if serial_start.hex() != "0100000053746172742a":
        errors.append("Serial Start frame invariant failed")
    return errors


def main() -> int:
    errors = check_links() + check_contract()
    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OK: 99 reference pages, local Markdown links, gRPC services, and Start frame invariants")
    return 0


if __name__ == "__main__":
    sys.exit(main())
