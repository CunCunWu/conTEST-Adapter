> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Recorder Documentation Attributes

Required License: CTX 000

In conTEST the user can append a documentation to the recorded file. The structure of the documentation and its attributes can be configured in the Recorder Configuration of a profile. Once the documentation is set up, the values of the attributes can be set using this network interface.

The client can initially inquire about the attributes of the documentation in the currently active profile (refer to the details below). Subsequently, the client can set the value of an attribute by sending the corresponding message containing the identifier of the attribute and the desired value (refer to Set Recorder Documentation Attribute Value).

## Get Recorder Documentation Attributes

The following message requests a list of all writable attributes of the recorder documentation in the currently active profile:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 41 |  | * | *Get Recorder Documentation Attributes Response* (ID:42) |

The content of this specific message has to be empty. The host will respond with *Get Recorder Documentation Attributes Response* (ID:42).

## Get Recorder Documentation Attributes Response

Upon receipt of the *Get Recorder Documentation Attributes* message, the host sends the subsequent message containing a list of the available attributes:

| ID | Content | Terminator | Example |
| --- | --- | --- | --- |
| 42 | {List of attribute informations ({Identifier;DataType}) seperated by comma (',')} | * | Car@Model;Text,Car@Engine@Displacement;Real,Car@Engine@Power;Integer |

In the message content, each attribute is seperated by a comma (','). In the given example, the substring containing the information of the first attribute is "Car@Model;Text". This represents a tuple consisting of the identifier and the data type, where its values are seperated by a semicolon (';'). The identifier is composed of the name of the attribute and its position in the documentation tree, i.e. the subforms. These parts are seperated by '@'. In the example, the first attributes name is "Model" in subform "Car" and the value is of type "Text". The second attribute is named "Displacement" in subform "Engine" in subform "Car" and is of type "Real". Should the name of a subform or attribute contain an '@', the character is escaped by a preceding backslash: "\@".

The following data types are possible:

- Text

- Integer

- Real

- Boolean

- DateTime

The identifier of the attributes can be used to set their values (refer to Set Recorder Documentation Attribute Value).
