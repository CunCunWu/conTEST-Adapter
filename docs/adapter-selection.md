# 适配器选择

## 推荐决策

| 需求 | 首选 | 原因 | 备选/注意 |
| --- | --- | --- | --- |
| 新项目，能使用 Protobuf/gRPC | gRPC | 强类型；请求/响应与流式订阅清晰；契约集中 | 仍需从 conTEST 设置取得 endpoint |
| 只想用标准 socket，或集成 PLC/嵌入式网络端 | TCP/IP | 无 broker；帧格式简单 | 必须自己实现拆包、little-endian ID、文本转义 |
| 多个消费者、跨网络解耦、需要最新状态保留 | MQTT | topic 清晰；conTEST 发布消息 retained | 需要外部 broker；要识别 retained 旧状态 |
| 目标环境无网络但有 COM 口 | Serial | 与 TCP/IP 的消息 ID/文本模型基本一致 | 需要 `*` 终止符；正文禁止 `*`；串口参数部分固定 |
| 只需硬接线启动/停止和灯/继电器状态 | Digital I/O | 不写网络协议；适合简单联锁 | 功能远少于其他 Adapter；active-low/active-high 不可接反 |

## 不应仅凭偏好决定的因素

- **功能覆盖**：Digital I/O 只有受限功能；其余接口虽覆盖面较大，但 Live Monitoring 的本地帮助存在缺页。
- **许可证**：先看具体接口页。能连接 Adapter 不等于具有 CTM 010/CTM 020 功能。
- **运行环境**：gRPC 需要生成语言绑定；MQTT 需要 broker；Serial 依赖物理串口；DIO 依赖支持的 Advantech 设备。
- **可观测性**：MQTT retained 很适合取“最近状态”，但事件新旧语义需要应用层处理；gRPC stream 和 TCP/Serial subscription 更接近会话型订阅。
- **安全**：原帮助没有给出 TLS、认证或网络隔离策略。不要假设协议默认加密；部署时由目标环境明确网络与凭据策略。

## 选择完成后

- gRPC：[Overview](../reference/GrpcAdapter/integration.md) · [Proto](../protocol/grpc/CtGrpcRemote.proto)
- TCP/IP：[Overview](../reference/TcpIpAdapter/integration.md) · [帧规则](tcp-serial-protocol.md)
- MQTT：[Overview](../reference/MQTTAdapter/integration.md)
- Serial：[Overview](../reference/SerialAdapter/integration.md) · [帧规则](tcp-serial-protocol.md)
- Digital I/O：[Overview](../reference/DIOAdapter/integration.md) · [Inputs](../reference/DIOAdapter/inputs.md) · [Outputs](../reference/DIOAdapter/outputs.md)
