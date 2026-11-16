# conTEST 1.15 Adapter Agent Guide

本仓库把本机安装的 **conTEST 1.15 ContinuousTesting Adapter** 帮助整理成一套适合人和 AI agent 使用的接口知识库。目标不是替代 conTEST 配置界面，而是让实现者能够快速选型、找到精确协议，并在不猜测字段、端口或许可证的前提下完成集成。

> 版本边界：内容来自 `C:\Program Files\conTEST 1.15\Documentation\ContinuousTesting Adapter`。如果目标机器不是 1.15，请先与该版本随附帮助核对。

## 从这里开始

1. Agent 先读 [AGENTS.md](AGENTS.md)，遵守版本、许可证和协议约束。
2. 用 [适配器选择](docs/adapter-selection.md) 决定 gRPC、TCP/IP、MQTT、Serial 或 Digital I/O。
3. 用 [能力索引](docs/capability-index.md) 从任务反查接口。
4. 实现 TCP/IP 或 Serial 前必读 [二进制帧与转义规则](docs/tcp-serial-protocol.md)。
5. 按 [常见调用流程](docs/recipes.md) 组织状态订阅、录制和结果处理。
6. 最后进入 [`reference/`](reference/) 查看精确方法、消息 ID、topic、字段和返回值。

## 五类适配器

| 适配器 | 适合场景 | 关键特征 | 精确参考 |
| --- | --- | --- | --- |
| gRPC | 新开发、强类型、多语言 RPC、流式订阅 | Protobuf；一元调用与 server stream；仓库含提取的 `.proto` | [gRPC](reference/GrpcAdapter/integration.md) |
| TCP/IP | PLC/脚本/既有 socket 系统；网络直连 | 4 字节 little-endian ID + UTF-8 内容 | [TCP/IP](reference/TcpIpAdapter/integration.md) |
| MQTT | 多设备、broker 解耦、保留状态、跨网络订阅 | 外部 broker；topic/payload；conTEST 发布消息均 retained | [MQTT](reference/MQTTAdapter/integration.md) |
| Serial | 无网络或串口控制器 | 与 TCP/IP 相同 ID/内容模型，但每帧以 `*` 终止 | [Serial](reference/SerialAdapter/integration.md) |
| Digital I/O | 最少功能的硬接线联锁/PLC | 输入 active-low，输出 active-high；只支持有限控制/状态 | [Digital I/O](reference/DIOAdapter/integration.md) |

## 快速事实

- conTEST 必须已经安装、配置并运行；要使用的 Adapter 需要在 conTEST 设置中启用。
- TCP/IP/Serial 的前 4 字节是 **32 位 little-endian 消息 ID**，后续是 UTF-8、Invariant/English 文本。
- TCP/IP/Serial 文本里的 `,` 和 `;` 必须用反斜杠转义。Serial 另外禁止在正文中使用 `*`，因为 `*` 是终止符。
- MQTT 的 broker 地址、端口和 top-level topic 来自 conTEST Adapter 设置；不要从本仓库猜默认值。
- gRPC 的服务地址/端口同样来自实际 conTEST 设置；[CtGrpcRemote.proto](protocol/grpc/CtGrpcRemote.proto) 是本地 1.15 帮助中给出的契约。
- CTX 000 是多项远程控制功能的基础许可证；后处理通常还要求 CTM 010，Condition Monitoring 通常还要求 CTM 020；Digital I/O Overview 另外写明 remoting 需要 CTX 100。以具体页面的 `Required License(s)` 为准。

## 仓库结构

```text
AGENTS.md                    Agent 的强制工作规则
docs/                        中文导航、选型、协议和流程
protocol/grpc/               从 1.15 帮助提取的 Protobuf 契约
reference/                   按 Adapter 分类的 99 个精确参考页面
tools/extract_contest_docs.py 可复现的本地帮助提取器
```

## 已知边界

- 本仓库只记录接口契约，没有目标设备的 IP、端口、COM 口、baudrate、MQTT 凭据或 top-level topic。
- 原帮助目录的 TOC 提到了 Live Monitoring 页面，但该安装目录缺少这些独立 HTML 页面；gRPC 的 Live Monitoring 契约仍可在 `.proto` 中找到。TCP/IP、Serial、MQTT 的 Live Monitoring 只能使用 Overview 中列出的 ID/topic，再结合目标安装的帮助或实机验证，不能凭空补全 payload。
- Digital I/O 原帮助在型号文字中同时出现 `USB-5750` 与 `USB-4750`，存在不一致；接线或采购前必须以 conTEST 设置中实际识别的设备和厂商手册核对。
- 未进行连接到实际 conTEST 实例的运行时验证；仓库校验覆盖提取完整性、Markdown 链接和基础协议示例。

## 来源与版权

详见 [来源、版本与再生成](docs/source-and-version.md) 和 [NOTICE](NOTICE.md)。
