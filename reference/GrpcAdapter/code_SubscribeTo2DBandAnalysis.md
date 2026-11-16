> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeTo2DBandAnalysis(SubscribeToAnalysisRequest) returns (stream Analysis2DBandResponse);

message SubscribeToAnalysisRequest { string id = 1; string analysisName = 2; }

message Analysis2DBandResponse { string analysisName = 1; string channelName = 2; repeated float value = 3; string unit = 100; double first = 101; double last = 102; string bandType = 103; }
