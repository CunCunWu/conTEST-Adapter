> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Set Processing Variable

Required Licenses: CTX 000, CTM 010

The used processing specification (hpsx) may contain processing variables for fine tuning an evaluation. The values of these processing variable can be set by the client. Initially, the client has the option to inquire about the available processing variables (refer to Get Processing Variables). Subsequently, the client can set the value of a specific processing variable using its name (refer to the details below).

## Set Processing Variable

The client can set the value of a processing variable with the following message:

| ID | Content | Response |
| --- | --- | --- |
| 19 | {VariableName},{Value} | *Set Processing Variable Response* (ID: 20) |

"{VariableName}" and "{Value}" are placeholders and have to be replaced by the name of the processing variable und the desired value, respectively.

As indication to the client that the host has successfully received and processed the message, the host will issue the response *Set Processing Variable Response* (ID:20).

## Set Processing Variable Response

When the *Set Processing Variable* message is received, the host sends the subsequent message as an indication to the client that the message has been successfully received and processed:

| ID | Content |
| --- | --- |
| 20 | True |
