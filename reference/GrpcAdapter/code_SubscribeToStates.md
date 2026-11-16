> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeToStates(SubscriptionRequest) returns (stream SubscribeToStatesResponse);

message SubscriptionRequest { string id = 1; }

message SubscribeToStatesResponse { ModuleStates states = 1; }

message ModuleStates { ModuleState RecorderState = 1; ModuleState AnalysisState = 2; ModuleState EvaluatorState = 3; }

enum ModuleState { Disabled = 0; Idle = 1; Running = 2; }
