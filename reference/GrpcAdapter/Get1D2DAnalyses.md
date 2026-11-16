> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## Get1DAnalyses, Get2DEquidistantAnalyses and Get2DBandAnalyses

The recorder in conTEST can be set up to continuously analyze the signal. These analyses can provide single values like the level or be more complex like a FFT. Calling *Get1DAnalyses* returns a list of single value analyses identified by their names. 2D analyses are devided into two groups. The first group contains analyses that have an equidistant abscissa. For example a FFT is attributed to this group. The second group contains analyses with band abscissas. An order spectrum can be found in this group. A list of names of the configured analyses can be received by calling *Get2DEquidistantAnalyses* and *Get2DBandAnalyses* for analyses with equidistant and band abscissa, respectively. The client can subscribe to the analyses via SubscribeTo1DAnalysis or SubscribeTo2DEquidistantAnalysis or SubscribeTo2DBandAnalysis.

- Get1DAnalyses

- Get2DEquidistantAnalyses

- Get2DBandAnalyses

```text
rpc Get1DAnalyses(Get1DAnalysesRequest) returns (Get1DAnalysesResponse);

message Get1DAnalysesRequest {
}

message Get1DAnalysesResponse {
    repeated string AnalysesNames = 1;
}
```

```text
rpc Get2DEquidistantAnalyses(Get2DEquidistantAnalysesRequest) returns (Get2DEquidistantAnalysesResponse);

message Get2DEquidistantAnalysesRequest {
}

message Get2DEquidistantAnalysesResponse {
    repeated string AnalysesNames = 1;
}
```

```text
rpc Get2DBandAnalyses(Get2DBandAnalysesRequest) returns (Get2DBandAnalysesResponse);

message Get2DBandAnalysesRequest {
}

message Get2DBandAnalysesResponse {
    repeated string AnalysesNames = 1;
}
```
