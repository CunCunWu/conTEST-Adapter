> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## SubscribeToStates

To be continuously informed about state changes of the recorder, analysis and evaluation in conTEST you can subscribe to changes using *SubscribeToStates*. Doing so provides a streaming object that delivers above mentioned states once they change. Each state can be *Disabled*, *Idle* or *Running*.

- SubscribeToStates

```text
rpc SubscribeToStates(SubscriptionRequest) returns (stream SubscribeToStatesResponse);

message SubscriptionRequest {
    string id = 1;
}

message SubscribeToStatesResponse {
    ModuleStates states = 1;
}

message ModuleStates {
    ModuleState RecorderState = 1;
    ModuleState AnalysisState = 2;
    ModuleState EvaluatorState = 3;
}

enum ModuleState {
    Disabled = 0;
    Idle = 1;
    Running = 2;
}
```
