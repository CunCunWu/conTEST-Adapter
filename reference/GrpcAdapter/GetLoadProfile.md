> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## GetProfiles and LoadProfile

conTEST can be configured to know several profiles with different recorder settings, processing specification or evaluation rule sets. To get a list of known profiles the *GetProfiles* procedure can be called returning a list of names of the profiles. To load a specific profile use *LoadProfile* and provide the respective name. Calling this procedure return wheather the request was successful.

- GetProfiles

- LoadProfile

```text
rpc GetProfiles(GetProfilesRequest) returns (GetProfilesResponse);

message GetProfilesRequest {
}

message GetProfilesResponse {
    repeated string profiles = 1;
}
```

```text
rpc LoadProfile(LoadProfileRequest) returns (LoadProfileResponse);

message LoadProfileRequest {
    string profile = 1;
}

message LoadProfileResponse {
    bool success = 1;
}
```
