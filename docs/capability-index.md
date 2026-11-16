# 能力索引

先按“要做什么”定位，再进入所选 Adapter 的精确页面。`—` 表示本地 1.15 帮助没有给出等价独立页面，不代表所有版本绝对不支持。

| 能力 | gRPC | TCP/IP | Serial | MQTT | Digital I/O |
| --- | --- | --- | --- | --- | --- |
| 开始/停止录制 | [Start/Stop](../reference/GrpcAdapter/StartStopRecord.md) | [Recorder Control](../reference/TcpIpAdapter/RecorderControl.md) | [Recorder Control](../reference/SerialAdapter/RecorderControl.md) | [Recorder Control](../reference/MQTTAdapter/RecorderControl.md) | [Inputs](../reference/DIOAdapter/inputs.md) |
| 设置 Custom Name | [SetCustomName](../reference/GrpcAdapter/SetCustomName.md) | [CustomName](../reference/TcpIpAdapter/CustomName.md) | [CustomName](../reference/SerialAdapter/CustomName.md) | [CustomName](../reference/MQTTAdapter/CustomName.md) | — |
| 获取/切换 Profile | [Profiles](../reference/GrpcAdapter/GetLoadProfile.md) | [Get](../reference/TcpIpAdapter/GetProfiles.md) / [Load](../reference/TcpIpAdapter/LoadProfile.md) | [Get](../reference/SerialAdapter/GetProfiles.md) / [Load](../reference/SerialAdapter/LoadProfile.md) | [Profiles](../reference/MQTTAdapter/Profiles.md) | — |
| 状态 | [States](../reference/GrpcAdapter/SubscribeToStates.md) | [States](../reference/TcpIpAdapter/States.md) | [States](../reference/SerialAdapter/States.md) | [States](../reference/MQTTAdapter/States.md) | [Outputs](../reference/DIOAdapter/outputs.md) |
| 最终结果 | [Results](../reference/GrpcAdapter/SubscribeToResults.md) | [Results](../reference/TcpIpAdapter/Results.md) | [Results](../reference/SerialAdapter/Results.md) | [Result](../reference/MQTTAdapter/Result.md) | [Outputs](../reference/DIOAdapter/outputs.md) |
| Processing Variables | [Get/Set](../reference/GrpcAdapter/GetSetVariables.md) | [Get](../reference/TcpIpAdapter/GetProcessingVariables.md) / [Set](../reference/TcpIpAdapter/SetProcessingVariable.md) | [Get](../reference/SerialAdapter/GetProcessingVariables.md) / [Set](../reference/SerialAdapter/SetProcessingVariable.md) | [Variables](../reference/MQTTAdapter/Variables.md) | — |
| Recorder Documentation | [Get/Set](../reference/GrpcAdapter/GetSetRecorderDocumentationAttributes.md) | [Get](../reference/TcpIpAdapter/GetRecorderDocumentationAttributes.md) / [Set](../reference/TcpIpAdapter/SetRecorderDocumentationAttributeValue.md) | [Get](../reference/SerialAdapter/GetRecorderDocumentationAttributes.md) / [Set](../reference/SerialAdapter/SetRecorderDocumentationAttributeValue.md) | [Documentation](../reference/MQTTAdapter/Documentation.md) | — |
| 1D/2D Analysis 列表 | [Get](../reference/GrpcAdapter/Get1D2DAnalyses.md) | [1D](../reference/TcpIpAdapter/GetAnalyses1D.md) / [2D equal](../reference/TcpIpAdapter/GetAnalyses2DEquidistant.md) / [2D band](../reference/TcpIpAdapter/GetAnalyses2DBand.md) | [1D](../reference/SerialAdapter/GetAnalyses1D.md) / [2D equal](../reference/SerialAdapter/GetAnalyses2DEquidistant.md) / [2D band](../reference/SerialAdapter/GetAnalyses2DBand.md) | [Analyses](../reference/MQTTAdapter/Analyses.md) | — |
| 1D/2D Analysis 订阅 | [Subscribe](../reference/GrpcAdapter/Subscribe1D2DAnalysis.md) | [1D](../reference/TcpIpAdapter/SubscribeAnalysis1D.md) / [2D equal](../reference/TcpIpAdapter/SubscribeAnalysis2DEquidistant.md) / [2D band](../reference/TcpIpAdapter/SubscribeAnalysis2DBand.md) | [1D](../reference/SerialAdapter/SubscribeAnalysis1D.md) / [2D equal](../reference/SerialAdapter/SubscribeAnalysis2DEquidistant.md) / [2D band](../reference/SerialAdapter/SubscribeAnalysis2DBand.md) | [Analyses](../reference/MQTTAdapter/Analyses.md) | — |
| Condition Monitoring | [Get/Subscribe](../reference/GrpcAdapter/GetSubscribeConditionMonitoring.md) | [Get](../reference/TcpIpAdapter/GetMonitoringConditions.md) / [Subscribe](../reference/TcpIpAdapter/SubscribeConditionMonitoring.md) / [Set](../reference/TcpIpAdapter/SetConditionMonitoringThreshold.md) | [Get](../reference/SerialAdapter/GetMonitoringConditions.md) / [Subscribe](../reference/SerialAdapter/SubscribeConditionMonitoring.md) / [Set](../reference/SerialAdapter/SetConditionMonitoringThreshold.md) | [Conditions](../reference/MQTTAdapter/Conditions.md) | [Inputs](../reference/DIOAdapter/inputs.md) / [Outputs](../reference/DIOAdapter/outputs.md) |
| 许可证状态 | [Proto methods](../protocol/grpc/CtGrpcRemote.proto) | [IsLicensed](../reference/TcpIpAdapter/IsLicensed.md) | [IsLicensed](../reference/SerialAdapter/IsLicensed.md) | [Licences](../reference/MQTTAdapter/Licences.md) | — |
| System Events | [Events](../reference/GrpcAdapter/SubscribeToSystemEvents.md) | [Events](../reference/TcpIpAdapter/SubscribeToSystemEvents.md) | [Events](../reference/SerialAdapter/SubscribeToSystemEvents.md) | [Events](../reference/MQTTAdapter/SystemEvents.md) | — |
| Live Monitoring | [Proto](../protocol/grpc/CtGrpcRemote.proto) | [Overview IDs](../reference/TcpIpAdapter/integration.md) | [Overview IDs](../reference/SerialAdapter/integration.md) | [Overview topic](../reference/MQTTAdapter/integration.md) | — |

## 许可速查

| 许可证 | 文档中的典型用途 |
| --- | --- |
| CTX 000 | 多数录制/远程调用的基础要求 |
| CTM 010 | Postprocessing、evaluation results、processing variables 等后处理能力 |
| CTM 020 | Online analyses / Condition Monitoring 相关能力 |
| CTX 100 | Digital I/O Overview 写明的 remoting 要求 |

此表只用于导航。实现前必须以具体接口页面的 `Required License(s)` 为准。
