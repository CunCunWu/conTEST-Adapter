> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeTo1DAnalysis(SubscribeToAnalysisRequest) returns (stream Analysis1DResponse);

message SubscribeToAnalysisRequest { string id = 1; string analysisName = 2; }

message Analysis1DResponse { string analysisName = 1; string channelName = 2; double value = 3; string unit = 4; }
