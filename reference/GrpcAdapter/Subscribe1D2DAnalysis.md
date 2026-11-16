> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## SubscribeTo1DAnalysis, SubscribeTo2DEquidistantAnalysis and SubscribeTo2DBandAnalysis

The list of provided analyses names can be used to subscribe to respective analyses using *SubscribeTo1DAnalysis*, *SubscribeTo2DEquidistantAnalysis* and *SubscribeTo2DBandAnalysis*. Doing so provides a streaming object of type *Analysis1DResponse*, *Analysis2DEquidistantResponse* or *Analysis2DBandResponse* that contain either a single value or an array of values and further information. conTEST is continuously sending these analyses until cancelled by the client.

- SubscribeTo1DAnalysis

- SubscribeTo2DEquidistantAnalysis

- SubscribeTo2DBandAnalysis

```text
rpc SubscribeTo1DAnalysis(SubscribeToAnalysisRequest) returns (stream Analysis1DResponse);

message SubscribeToAnalysisRequest {
    string id = 1;
    string analysisName = 2;
}

message Analysis1DResponse {
    string analysisName = 1;
    string channelName = 2;
    double value = 3;
    string unit = 4;
}
```

```text
rpc SubscribeTo2DEquidistantAnalysis(SubscribeToAnalysisRequest) returns (stream Analysis2DEquidistantResponse);

message SubscribeToAnalysisRequest {
    string id = 1;
    string analysisName = 2;
}

message Analysis2DEquidistantResponse {
    string analysisName = 1;
    string channelName = 2;
    repeated float value = 3;
    string unit = 100;
    double first = 101;
    double delta = 102;
    string abscissaUnit = 103;
}
```

```text
rpc SubscribeTo2DBandAnalysis(SubscribeToAnalysisRequest) returns (stream Analysis2DBandResponse);

message SubscribeToAnalysisRequest {
    string id = 1;
    string analysisName = 2;
}

message Analysis2DBandResponse {
    string analysisName = 1;
    string channelName = 2;
    repeated float value = 3;
    string unit = 100;
    double first = 101;
    double last = 102;
    string bandType = 103;
}
```
