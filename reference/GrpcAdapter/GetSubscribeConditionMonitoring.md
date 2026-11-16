> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## GetMonitoringConditions and SubscribeToConditionMonitoring

When Condition Monitoring is configured in conTEST, clients can subscribe to receive continuous updates on whether the condition is met or not.

The client can initially inquire about the available conditions. Subsequently, the client can start the subscription by sending the corresponding message containing the ID of the condition. Doing so provides a streaming object of type *SubscribeToConditionMonitoringResponse* that contains information about the condition and whether the results of the analysis are out of bounds or not. conTEST is continuously sending change updates until cancelled by the client.

- Get Available Monitoring Conditions

- Subscribe To Condition Monitoring

```text
rpc GetMonitoringConditions(GetMonitoringConditionsRequest) returns (GetMonitoringConditionsResponse);

message GetMonitoringConditionsRequest {
}

message GetMonitoringConditionsResponse {
    repeated MonitoringCondition conditions = 1;
}

message MonitoringCondition{
    string id = 1;
    string name = 2;
}
```

```text
rpc SubscribeToConditionMonitoring(SubscribeToConditionMonitoringRequest) returns (stream SubscribeToConditionMonitoringResponse);

message SubscribeToConditionMonitoringRequest {
    string id = 1;
}

message SubscribeToConditionMonitoringResponse {
    string id = 1;
    bool isOutOfBounds = 2;
}
```
