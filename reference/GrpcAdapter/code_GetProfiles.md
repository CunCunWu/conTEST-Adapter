> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc GetProfiles(GetProfilesRequest) returns (GetProfilesResponse);

message GetProfilesRequest { }

message GetProfilesResponse { repeated string profiles = 1; }
