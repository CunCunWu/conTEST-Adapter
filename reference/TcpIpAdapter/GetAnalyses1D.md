> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Available Analyses 1D

Required Licenses: CTX 000, CTM 020

The recorder in conTEST can be set up to continuously analyze the signal. These analyses can provide single values like the level or be more complex like a FFT. This message returns a list of single value analyses identified by their names. The client can subscribe to the analyses via Subscribe To 1D Analysis.

## Get Available Analyses 1D

The client can request a list of the available single value analyses with the following message:

| ID | Content | Response |
| --- | --- | --- |
| 21 |  | *Get Available Analyses 1D Response* (ID:22) |

The content of this message has to be empty. The host will respond with *Get Available Analyses 1D Response* (ID:22).

## Get Available Analyses 1D Response

When the *Get Available Analyses 1D* message is received, the host sends the subsequent message containing a list of the available analyses names:

| ID | Content | Example |
| --- | --- | --- |
| 22 | {List of analyses names separated by comma (',')} | Analysis 1,Analysis 2,Analysis 3 |

These names can be used to start the subscription (refer to Subscribe To Analysis 1D).
