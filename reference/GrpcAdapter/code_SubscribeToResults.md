> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SubscribeToResults(SubscriptionRequest) returns (stream SubscribeToResultsResponse);

message SubscriptionRequest { string id = 1; }

message SubscribeToResultsResponse { string id = 1; google.protobuf.Timestamp Timestamp = 2; string CustomName = 3; RecordingSummary recordingSummary = 4; CalculationSummary calculationSummary = 5; EvaluationSummary evaluationSummary = 6; }

message RecordingSummary{ string File = 1; Result success = 2; }

enum Result { Failed = 0; Succeeded = 1; }

message CalculationSummary { Result OverallSuccess = 1; repeated CalculationResult Results = 2; }

message CalculationResult { string Name = 1; Result Success =2; repeated string ResultFiles =3; repeated string Errors =4; }

message EvaluationSummary { Result OverallSuccess = 1; string Classification = 2; repeated EvaluationResult Results = 3; }

message EvaluationResult { string ResultName =1; bool Success =2; string Filename =3; string ChannelName =4; Tolerance Tolerance =5; SingleValue SingleValue =6; repeated string Errors =100; }

message Tolerance { string Name = 1; ToleranceRole Role = 2; double Limit = 3; }

enum ToleranceRole { None = 0; Lower = 1; Upper =2; }

message SingleValue { string Name = 1; double Value =2; string Unit = 3; string Quantity = 4; }
