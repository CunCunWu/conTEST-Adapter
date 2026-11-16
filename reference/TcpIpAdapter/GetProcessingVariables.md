> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Processing Variables

Required Licenses: CTX 000, CTM 010

The used processing specification (hpsx) may contain processing variables for fine tuning an evaluation. The values of these processing variable can be set by the client. Initially, the client has the option to inquire about the available processing variables (refer to details below). Subsequently, the client can set the value of a specific processing variable using its name (refer to Set Processing Variable).

## Get Processing Variables

The client can request a list of all available processing variables with following message:

| ID | Content | Response |
| --- | --- | --- |
| 17 |  | *Get Processing Variables Response* (ID:18) |

The content of this message has to be empty. The host will respond with *Get Processing Variables Response* (ID:18).

## Get Processing Variables Response

When the *Get Processing Variables* message is received, the host sends the subsequent message containing a list of the available processing variables:

| ID | Content | Example |
| --- | --- | --- |
| 18 | {List of variable names separated by comma (',')} | Variable 1,Variable 2,Variable 3 |

The names of the processing variables can be used to set the respective values (refer to Set Processing Variable).
