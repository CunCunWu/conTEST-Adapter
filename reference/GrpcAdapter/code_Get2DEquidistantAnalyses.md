> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc Get2DEquidistantAnalyses(Get2DEquidistantAnalysesRequest) returns (Get2DEquidistantAnalysesResponse);

message Get2DEquidistantAnalysesRequest { }

message Get2DEquidistantAnalysesResponse { repeated string AnalysesNames = 1; }
