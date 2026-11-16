> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc StopRecord(StopRecordRequest) returns (StopRecordReply);

message StopRecordRequest { }

message StopRecordReply { bool stopped = 1; }
