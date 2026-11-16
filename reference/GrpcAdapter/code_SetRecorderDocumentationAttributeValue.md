> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

rpc SetRecorderDocumentationAttributeValue(SetRecorderDocumentationAttributeValueRequest) returns (SetRecorderDocumentationAttributeValueResponse);

message SetRecorderDocumentationAttributeValueRequest { string attributeIdentifier = 1; string value = 2; }

message SetRecorderDocumentationAttributeValueResponse { bool success = 1; }
