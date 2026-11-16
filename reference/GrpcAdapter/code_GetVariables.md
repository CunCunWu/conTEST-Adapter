> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc GetVariables(GetVariablesRequest) returns (GetVariablesReply);

message GetVariablesRequest { }

message GetVariablesReply { repeated string variables = 1; }
