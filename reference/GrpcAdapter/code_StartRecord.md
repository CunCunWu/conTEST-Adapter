> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc StartRecord(StartRecordRequest) returns (StartRecordReply);

message StartRecordRequest { }

message StartRecordReply { bool started = 1; }
