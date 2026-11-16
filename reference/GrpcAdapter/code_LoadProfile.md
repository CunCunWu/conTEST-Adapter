> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc LoadProfile(LoadProfileRequest) returns (LoadProfileResponse);

message LoadProfileRequest { string profile = 1; }

message LoadProfileResponse { bool success = 1; }
