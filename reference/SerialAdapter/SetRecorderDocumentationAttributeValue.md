> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Set Recorder Documentation Attribute Value

Required License: CTX 000

In conTEST the user can append a documentation to the recorded file. The structure of the documentation and its attributes can be configured in the Recorder Configuration of a profile. Once the documentation is set up, the values of the attributes can be set using this network interface.

The client can initially inquire about the attributes of the documentation in the currently active profile (refer to Get Recorder Documentation Attributes. Subsequently, the client can set the value of an attribute by sending the corresponding message containing the identifier of the attribute and the desired value (refer to the details below).

## Set Recorder Documentation Attribute Value

The client can set the value of a documentation attribute with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 43 | {Identifier},{Value} | * | *Set Recorder Documentation Attribute Value Response* (ID:44) |

"{Identifier}" und "{Value}" are placeholders and have to be replaced by the attribute identifier and the desired value, respectively. Example: "Car@Engine@Displacement,1.8".

As indication to the client that the host has successfully received and processed the message, the host will issue the response *Set Recorder Documentation Attribute Value Response* (ID:44).

## Set Recorder Documentation Attribute Value Response

Upon receipt of the *Set Recorder Documentation Attribute Value* message, the host sends the subsequent message as an indication to the client that the message has been successfully received and processed:

| ID | Content if successful | Content if failed | Terminator |
| --- | --- | --- | --- |
| 44 | True | False | * |

The content of the message contains "True" if the value was set successfully. The content is "False" should conTEST not find the corresponding attribute for the given identifier or the value could not be converted to the attributes data type.
