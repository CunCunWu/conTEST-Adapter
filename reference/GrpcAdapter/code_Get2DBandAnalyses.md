> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc Get2DBandAnalyses(Get2DBandAnalysesRequest) returns (Get2DBandAnalysesResponse);

message Get2DBandAnalysesRequest { }

message Get2DBandAnalysesResponse { repeated string AnalysesNames = 1; }
