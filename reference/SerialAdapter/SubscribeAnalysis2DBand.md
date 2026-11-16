> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To Analysis 2D Band

Required Licenses: CTX 000, CTM 020

The list of provided 2D band analyses names can be used to subscribe to respective analyses. conTEST is continuously sending updates about the subscribed analyses until the client unsubscribes from them.

## Subscribe To Analysis 2D Band

The client can start the subscription with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 31 | {SubscriptionID},{AnalysisName} | * | Subscription is started and analysis updates are sent to client with *Analysis 2D Band Update* messages (ID:32) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client. "{AnalysisName}" is a placeholder for the name of the desired analysis. To request a list of available analyses refer to Get Available Analyses 2D Band.

Once the host receives the subscription request, analysis updates are sent to the client in the form of *Analysis 2D Band Update* messages.

To cancel the subscription refer to Unsubscribe From Analysis.

## Analysis 2D Band Update

If a subscription is established, every time an update to the subscribed analysis is available, the host sends the following message to the client:

| ID | Content | Terminator |
| --- | --- | --- |
| 32 | {SubscriptionID},{AnalysisName},{ChannelName},{Unit},{BandType},{FirstAbscissaValue},{LastAbscissaValue},{List of values separated by comma (',')} | * |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{SubscriptionID}|Identifier for the analysis subscription| |{AnalysisName}|Name of the analysis| |{ChannelName}|Name of the analyzed channel| |{Unit}|Unit of the values| |{BandType}|Band type; for example "Octave3rd"| |{FirstAbscissaValue}|First value of the abscissa| |{LastAbscissaValue}|Last value of the abscissa| |{List of values separated by comma (',')}|Analysis values|

To indicate that the client has successfully received the message and is ready for the next update, they are expected to send the message Received Analysis 2D Update.
