> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## Get/Set Recorder Documentation Attributes

In conTEST the user can append a documentation to the recorded file. The structure of the documentation and its attributes can be configured in the Recorder Configuration of a profile. Once the documentation is set up, the values of the attributes can be set using this network interface.

The client can initially inquire about the attributes of the documentation in the currently active profile. Subsequently, the client can set the value of an attribute by using its identifier.

- Get Recorder Documentation Attributes

- Set Recorder Documentation Attribute Value

```text
rpc GetRecorderDocumentationAttributes(GetRecorderDocumentationAttributesRequest) returns (GetRecorderDocumentationAttributesResponse);

message GetRecorderDocumentationAttributesRequest {
}

message GetRecorderDocumentationAttributesResponse {
    repeated RecorderDocumentationAttribute attributes = 1;
}

message RecorderDocumentationAttribute {
    string identifier = 1;
    string dataType = 2;
}
```

The identifier is composed of the name of the attribute and its position in the documentation tree, i.e. the subforms. These parts are seperated by '@'. Example: "Car@Engine@Power". The attribute name is "Power" in subform "Engine" in subform "Car". Should the name of a subform or attribute contain an '@', the character is escaped by a preceding backslash: "\@".

The following data types are possible:

- Text

- Integer

- Real

- Boolean

- DateTime

```text
rpc SetRecorderDocumentationAttributeValue(SetRecorderDocumentationAttributeValueRequest) returns (SetRecorderDocumentationAttributeValueResponse);

message SetRecorderDocumentationAttributeValueRequest {
    string attributeIdentifier = 1;
    string value = 2;
}

message SetRecorderDocumentationAttributeValueResponse {
    bool success = 1;
}
```

The host responds with "True" if setting the value was successful. Should conTEST not find the corresponding attribute for the given identifier or the value could not be parsed to the attributes data type, "False" is returned.
