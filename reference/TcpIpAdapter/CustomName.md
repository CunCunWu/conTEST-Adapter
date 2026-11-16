> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Custom Name

Required License: CTX 000

The custom name serves an optional additional identifier for the recording/result. For instance, it could be the serial number of the device being tested. Once the custom name is set, it will be attached as an attribute to all subsequent recordings/results until a new custom name is set.

## Set Custom Name

The client can use the following message to set the custom name:

| ID | Content | Response |
| --- | --- | --- |
| 3 | Set,{DesiredName} | *Custom Name Response* (ID:4) |

"{DesiredName}" is a placeholder for the desired custom name. For example, the content of the message could look like this: "Set,SN:123456789".

To reset the custom name, the placeholder "{DesiredName}" has to be empty: "Set,".

As indication to the client that the host has successfully received and processed the message, the host will issue the response *Custom Name Response* (ID:4).

## Custom Name Response

Upon receipt of the *Set Custom Name* message, the host sends the subsequent message as an indication to the client that the message has been successfully received and processed:

| ID | Content |
| --- | --- |
| 4 | True |
