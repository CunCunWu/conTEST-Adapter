> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## SubscribeToSystemEvents

To be continuously informed about system events of conTEST, you can subscribe to an event stream using the *SubscribeToSystemEvents* function. The events received are identical to those displayed on the dashboard in the events content and categorized as info, warning or error.

- SubscribeToSystemEvents

```text
rpc SubscribeToSystemEvents(SubscriptionRequest) returns (stream SubscribeToSystemEventsResponse);

message SubscriptionRequest {
    string id = 1;
}

message SubscribeToStatesResponse {
    ModuleStates states = 1;
}

message SubscribeToSystemEventsResponse {
    SystemEventType type = 1;
    google.protobuf.Timestamp timestamp = 2;
    string loggerName = 3;
    string message = 4;
}

enum SystemEventType {
    Info = 0;
    Warning = 1;
    Error = 2;
}
```
