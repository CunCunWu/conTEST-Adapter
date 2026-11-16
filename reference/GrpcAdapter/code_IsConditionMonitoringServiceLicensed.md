> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc IsConditionMonitoringServiceLicensed(IsConditionMonitoringServiceLicensedRequest) returns (IsConditionMonitoringServiceLicensedResponse);

message IsConditionMonitoringServiceLicensedRequest { }

message IsConditionMonitoringServiceLicensedResponse { bool isLicensed = 1; }
