> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To States

Required License: CTX 000

To be continuously informed about state changes of the recorder, processing and evaluation, the client can subscribe to changes using this message. Each state can be *Disabled*, *Idle* or *Running*.

## Subscribe To States

| ID | Content | Terminator | Effect |
| --- | --- | --- | --- |
| 9 | {SubscriptionID} | * | Subscription is started and state changes are sent to client with *State Update* messages (ID:10) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client.

Once the host receives the subscription request, subsequent updates regarding state changes are sent to the client in the form of *State Update* messages.

## State Update

If a subscription is established, every time the state of the recorder, processing or evaluation changes, the host sends the following message to the client:

| ID | Content | Terminator | Possible States |
| --- | --- | --- | --- |
| 10 | Recorder;{state},Processing;{state},Evaluation;{state} | * | Disabled, Idle, Running |

"{state}" is a placeholder for the current state and can be either "Disabled", "Idle" or "Running". For instance, when a recording is in progress, the content of the message appears as follows:

"Recorder;Running,Processing;Idle,Evaluation;Idle"

## Unsubscribe From States

The client can unsubscribe from state change updates with the following message:

| ID | Content | Terminator | Effect |
| --- | --- | --- | --- |
| 11 | {SubscriptionID} | * | Subscription with ID *SubscriptionID* is cancelled |

"{SubscriptionID}" is a placeholder for the identifier of the subscription to be cancelled.
