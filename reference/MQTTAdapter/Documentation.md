> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Documentation

Required License: CTX 000

Within conTEST, the user can append a documentation to the recorded file. The structure of the documentation and its attributes can be configured in the recorder configuration of each profile. Once the documentation is set up, the values of the attributes can be set locally or remotely.

The available attributes of the documentation are published on a dedicated topic. Furthermore, you can set the value of an attribute by publishing a message containing the identifier of the attribute and the desired value on another topic.

## Available Documentation Attributes

conTEST publishes the available documentation attributes on the topic

```text
{top-level-topic}/documentation/availableAttributes
```

The payload is a comma-separated string of pairs of attribute identifier and data type. The pair of identifier and data type is separated by a semicolon:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/documentation/availableAttributes` | "{FirstAttributeIdentifier};{FirstAttributeDataType},{SecondAttributeIdentifier};{SecondAttributeDataType}" |

## Set Documentation Attribute

conTest allows you to set a documentation attribute remotely by publishing on the topic

```text
{top-level-topic}/documentation/setAttribute
```

The payload must be a comma-separated string with a single pair of attribute identifier and new value. conTEST will try to match the provided identifier to a valid attribute name and try to set the attribute to the provided value. If the provided identifier is invalid, the attribute value will not change. Please refer to the published list of available documentation attributes to make sure you provide a valid identifier.

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/documentation/setAttribute` | "{AttributeIdentifier},{NewAttributeValue}" |
