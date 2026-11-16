> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To System Events

Required License: CTX 000

To be continuously informed about system events of conTEST, you can subscribe to an event stream using this message. The events received are identical to those displayed on the dashboard in the events content and categorized as info, warning or error.

## Subscribe To System Events

| ID | Content | Effect |
| --- | --- | --- |
| 45 | {SubscriptionID} | Subscription is started and new system events are sent to client with *New System Event* messages (ID:46) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client.

Once the host receives the subscription request, subsequent system events are sent to the client in the form of *New System Event* messages.

## New System Event

If a subscription is established, every time a new system event occurs in conTEST, the host sends the following message to the client:

| ID | Content |
| --- | --- |
| 46 | {Type},{Timestamp},{Source},{Message} |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{Type}|Type of the event. Is either "Info", "Warning", "Error"| |{Timestamp}|UTC timestamp| |{Source}|Component that triggered the event| |{Message}|Event message|

## Unsubscribe From System Events

The client can unsubscribe from system events with the following message:

| ID | Content | Effect |
| --- | --- | --- |
| 47 | {SubscriptionID} | Subscription with ID *SubscriptionID* is cancelled |

"{SubscriptionID}" is a placeholder for the identifier of the subscription to be cancelled.
