> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To Analysis 1D

Required Licenses: CTX 000, CTM 020

The recorder in conTEST can be set up to continuously analyze the current signal. For example, these analyses can provide single values like the level. The client can subscribe to the analyses and receive continuous updates (refer to the details below).

## Subscribe To Analysis 1D

The client can start the subscription with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 23 | {SubscriptionID},{AnalysisName} | * | Subscription is started and analysis updates are sent to client with *Analysis 1D Update* messages (ID:24) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client. "{AnalysisName}" is a placeholder for the name of the desired analysis. To request a list of available analyses refer to Get Available Analyses 1D.

Once the host receives the subscription request, analysis updates are sent to the client in the form of *Analysis 1D Update* messages.

To cancel the subscription refer to Unsubscribe From Analysis.

## Analysis 1D Update

If a subscription is established, every time an update to the subscribed analysis is available, the host sends the following message to the client:

| ID | Content | Terminator |
| --- | --- | --- |
| 24 | {AnalysisName},{ChannelName},{Value},{Unit} | * |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{AnalysisName}|Name of the analysis| |{ChannelName}|Name of the analyzed channel| |{Value}|Current value of the analysis| |{Unit}|Unit of the value|
