> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Received Analysis 2D Update

Required Licenses: CTX 000, CTM 020

It is expected that the client sends a message of this type to indicate that an update of a 2D band analysis or an update of a 2D equidistant analysis has successfully been received. Doing so flags that the client is ready to receive the next update of any 2D analysis. Analyses data is sent in a cyclic way.

## Received Analysis 2D Update

The client can signal a successful receive of an 2D analysis update with the following message:

| ID | Content | Response |
| --- | --- | --- |
| 35 | {SubscriptionID} | The next update of analysis data |

"{SubscriptionID}" is a placeholder for the identifier of the subscription to a specific 2D analysis.
