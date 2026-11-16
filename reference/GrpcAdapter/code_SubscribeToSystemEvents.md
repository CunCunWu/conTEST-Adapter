> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeToSystemEvents(SubscriptionRequest) returns (stream SubscribeToSystemEventsResponse);

message SubscriptionRequest { string id = 1; }

message SubscribeToStatesResponse { ModuleStates states = 1; }

message SubscribeToSystemEventsResponse { SystemEventType type = 1; google.protobuf.Timestamp timestamp = 2; string loggerName = 3; string message = 4; }

enum SystemEventType { Info = 0; Warning = 1; Error = 2; }
