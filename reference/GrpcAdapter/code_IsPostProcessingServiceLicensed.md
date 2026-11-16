> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc IsPostProcessingServiceLicensed(IsPostProcessingServiceLicensedRequest) returns (IsPostProcessingServiceLicensedResponse);

message IsPostProcessingServiceLicensedRequest { }

message IsPostProcessingServiceLicensedResponse { bool isLicensed = 1; }
