> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## StartRecord and StopRecord

Used to start/stop a record. The response contains the information wheather the record successfully *started*/*stopped*. Once a record stopped expect a result if subscribed to.

- StartRecord

- StopRecord

```text
rpc StartRecord(StartRecordRequest) returns (StartRecordReply);

message StartRecordRequest {
}

message StartRecordReply {
  bool started = 1;
}
```

```text
rpc StopRecord(StopRecordRequest) returns (StopRecordReply);

message StopRecordRequest {
}

message StopRecordReply {
     bool stopped = 1;
}
```
