> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc GetRecorderDocumentationAttributes(GetRecorderDocumentationAttributesRequest) returns (GetRecorderDocumentationAttributesResponse);

message GetRecorderDocumentationAttributesRequest { }

message GetRecorderDocumentationAttributesResponse { repeated RecorderDocumentationAttribute attributes = 1; }

message RecorderDocumentationAttribute { string identifier = 1; string dataType = 2; }
