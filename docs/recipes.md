# 常见调用流程

这些流程描述调用顺序；字段与返回值必须从对应 `reference/` 页面取得。

## 一次完整录制与结果处理

1. 确认 conTEST 已运行、Adapter 已启用，记录目标版本与 endpoint。
2. 检查 CTX 000 以及实际处理链需要的 CTM 010/CTM 020。
3. 建立状态订阅；不要用固定 sleep 猜测模块是否 ready。
4. 可选：发现并切换 Profile，等待 active/状态确认。
5. 可选：设置 Custom Name、Recorder Documentation Attributes、Processing Variables。
6. 建立结果订阅。
7. 发送 Start Record；确认成功或 recorder state 进入 Running。
8. 发送 Stop Record；继续观察 processing/evaluation 状态。
9. 收到最终结果后，分别处理 recording、calculation、evaluation 的成功/错误信息。
10. 正常取消订阅；断线时按幂等方式重连，避免把重复结果当成新结果。

入口：[能力索引](capability-index.md)。

## 在线 1D/2D 分析

1. 检查 CTM 020 及对应接口页要求。
2. 调用/订阅 available analyses，取得真实 analysis name；不要硬编码猜测名称。
3. 用唯一 subscription id 和 analysis name 建立订阅。
4. 对 1D 保存 `value` 与 `unit`；对 2D 同时保存横坐标定义（equidistant 的 first/delta/abscissaUnit，band 的 first/last/bandType）。
5. TCP/IP/Serial 的 2D 更新按 [Received Analysis 2D Update](../reference/TcpIpAdapter/ReceivedAnalysis2DUpdate.md) 处理确认/流控。
6. 结束时取消订阅；gRPC stream 则取消 RPC context。

## Condition Monitoring

1. 检查 CTM 020。
2. 先获取条件列表，保存服务返回的 condition ID、name、type 和当前 option。
3. 需要修改时，根据 type 设置 threshold 或 tolerance-file options，不能混用字段。
4. 建立订阅并用 condition ID 关联更新。
5. DIO 模式下，输入为 active-low；若启用了 “Require acknowledgement of condition monitoring NOK”，确认输入必须保持超过 polling time。

## MQTT 客户端启动顺序

1. 从 conTEST 设置读取 broker 和 top-level topic。
2. 先订阅需要的 state/result/event topic，再发布控制命令，避免错过快速状态变化。
3. conTEST 发布消息是 retained；连接后立即到达的消息可能是旧的最近值。
4. 对控制 topic 不要假设一定存在 response topic；具体页面若说明“无成功通知”，就用状态变化或后续读取验证。
5. 多台 conTEST 可用不同 top-level topic，例如 `conTEST/machine1/`、`conTEST/machine2/`，再用 broker wildcard 统一订阅。

## gRPC 客户端生成

1. 使用 [CtGrpcRemote.proto](../protocol/grpc/CtGrpcRemote.proto) 生成目标语言代码。
2. 配置实际 endpoint，不在代码中写假定端口。
3. 分别创建 `CtGrpcAdapter`、`PostProcessingService`、`ConditionMonitoringService`、`LiveMonitoringService` client；功能属于哪个 service 以 proto 为准。
4. 一元调用检查 bool success/started/stopped；stream 调用实现取消、异常和重连。
5. `EvaluationResult.ResultName` 在 proto 中标记 deprecated，不要为新代码建立依赖。
