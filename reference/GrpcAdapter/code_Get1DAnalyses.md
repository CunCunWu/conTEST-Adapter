> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc Get1DAnalyses(Get1DAnalysesRequest) returns (Get1DAnalysesResponse);

message Get1DAnalysesRequest { }

message Get1DAnalysesResponse { repeated string AnalysesNames = 1; }
