> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SetCustomName(CustomNameRequest) returns (CustomNameReply);

message CustomNameRequest { string customName = 1; }

message CustomNameReply {

}
