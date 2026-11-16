# TCP/IP 与 Serial 协议规则

## 共用帧主体

```text
+-------------------------+---------------------------+
| 4-byte message type ID  | UTF-8 text content        |
| uint32 little-endian    | invariant/English culture |
+-------------------------+---------------------------+
```

- 不要把 ID 写成 ASCII 文本。ID `1` 的 4 字节是 `01 00 00 00`。
- 文本必须按具体消息页给出的关键字、逗号和分号格式生成。
- `,` 与 `;` 是保留分隔符。值本身包含它们时，编码为 `\,` 与 `\;`。
- 接收端要做增量解析；网络或串口一次 read 返回的数据长度不等于一条消息长度。

## TCP/IP

TCP/IP Overview 只定义 4 字节 ID + UTF-8 内容，没有定义 `*` 终止符。不要把 Serial 的 `*` 规则复制到 TCP/IP。

开始录制示例：

```text
01 00 00 00 53 74 61 72 74
| message ID 1 |  "Start" |
```

精确 ID 映射见 [TCP/IP Overview](../reference/TcpIpAdapter/integration.md)。由于 Overview 没有给出通用长度字段，接收拆包必须结合目标消息格式和实际连接行为验证，尤其是连续到达的订阅更新。

## Serial

Serial 在共用帧主体后追加 `0x2A`，即 ASCII `*`：

```text
01 00 00 00 53 74 61 72 74 2A
| message ID 1 |  "Start" | * |
```

固定串口设置：8 data bits、no parity、1 stop bit。COM 口与 baudrate 在 conTEST Adapter 设置中指定。正文禁止出现 `*`，否则会被误判为帧结束。

## 最小编码伪代码

```python
def encode_frame(message_id: int, content: str, serial: bool = False) -> bytes:
    escaped = content.replace(",", "\\,").replace(";", "\\;")
    if serial and "*" in escaped:
        raise ValueError("Serial payload cannot contain '*'")
    frame = message_id.to_bytes(4, "little", signed=False) + escaped.encode("utf-8")
    return frame + (b"*" if serial else b"")
```

注意：原帮助只明确要求转义逗号和分号，没有定义反斜杠自身的转义规则。字段本身可能包含反斜杠时，不要猜测；应通过目标版本实机验证。

## 2D 流的流控

TCP/IP/Serial Overview 列出 `Received Analysis 2D Update`（client→host，ID 35），并有单独参考页。实现 2D 订阅时必须阅读该页，不要只消费更新而遗漏协议要求的确认：[TCP/IP](../reference/TcpIpAdapter/ReceivedAnalysis2DUpdate.md) / [Serial](../reference/SerialAdapter/ReceivedAnalysis2DUpdate.md)。
