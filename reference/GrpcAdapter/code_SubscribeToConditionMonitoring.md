> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeToConditionMonitoring(SubscribeToConditionMonitoringRequest) returns (stream SubscribeToConditionMonitoringResponse);

message SubscribeToConditionMonitoringRequest { string id = 1; }

message SubscribeToConditionMonitoringResponse { string id = 1; bool isOutOfBounds = 2; }
