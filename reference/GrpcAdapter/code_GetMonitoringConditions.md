> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc GetMonitoringConditions(GetMonitoringConditionsRequest) returns (GetMonitoringConditionsResponse);

message GetMonitoringConditionsRequest { }

message GetMonitoringConditionsResponse { repeated MonitoringCondition conditions = 1; }

message MonitoringCondition{ string id = 1; string name = 2; }
