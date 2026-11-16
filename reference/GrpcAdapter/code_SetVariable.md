> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SetVariable(SetVariableRequest) returns (SetVariableReply);

message SetVariableRequest { string name = 1; string value = 2; }

message SetVariableReply { }
