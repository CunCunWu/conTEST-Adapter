> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Available Analyses 2D Equidistant

Required Licenses: CTX 000, CTM 020

The recorder in conTEST can be set up to continuously analyze the signal. 2D analyses are devided into two groups. The first group contains analyses that have an equidistant abscissa. For example a FFT is attributed to this group. A list of names of the configured analyses can be received by sending this message. The second group contains analyses with band abscissas (refer to Get Available Analyses 2D Band). For example, an octave spectrum can be found in that group.

The client can subscribe to the analyses via Subscribe To 2D Equidistant Analysis.

## Get Available Analyses 2D Equidistant

The client can request a list of the available 2D equidistant analyses with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 25 |  | * | *Get Available Analyses 2D Equidistant Response* (ID:26) |

The content of this message has to be empty. The host will respond with *Get Available Analyses 2D Equidistant Response* (ID:26).

## Get Available Analyses 2D Equidistant Response

When the *Get Available Analyses 2D Equidistant* message is received, the host sends the subsequent message containing a list of the available analyses names:

| ID | Content | Terminator | Example |
| --- | --- | --- | --- |
| 26 | {List of analyses names separated by comma (',')} | * | Analysis 1,Analysis 2,Analysis 3* |

These names can be used to start the subscription (refer to Subscribe To Analysis 2D Equidistant).
