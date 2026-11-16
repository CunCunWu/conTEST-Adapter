> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To Condition Monitoring

Required Licenses: CTX 000, CTM 020

When Condition Monitoring is configured in conTEST, clients can subscribe to receive continuous updates on whether the condition is met or not.

The client can initially inquire about the available conditions (refer to Get Available Monitoring Conditions). Subsequently, the client can start the subscription by sending the corresponding message containing the ID of the condition (refer to the details below).

## Subscribe To Condition Monitoring

The client can start the subscription with the following message:

| ID | Content | Effect |
| --- | --- | --- |
| 47 | {SubscriptionID},{ConditionID} | Subscription is started and updates are sent to client with *Condition Monitoring Update* messages (ID:48) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client. "{ConditionID}" is a placeholder for the ID of the desired condition. To request a list of available conditions refer to Get Available Monitoring Conditions.

Once the host receives the subscription request, change updates are sent to the client in the form of *Condition Monitoring Update* messages.

To cancel the subscription refer to the details below.

## Condition Monitoring Update

If a subscription is established, every time the state of the monitored condition changes, the host sends the following message to the client:

| ID | Content |
| --- | --- |
| 48 | {ConditionID},{IsWithinBounds} |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{ConditionID}|ID of the condition| |{IsWithinBounds}|Indicates whether the analysis results are within bounds or not. Can be either "True" or "False"|

Example: conTEST is configured to monitor that the level does not exceed 80dB. Should the level exceed this value the state {IsWithinBounds} would be "False". If the level drops below the threshold the state would be "True".

## Unsubscribe From Results

The client can unsubscribe from condition monitoring updates with the following message:

| ID | Content | Response |
| --- | --- | --- |
| 49 | {SubscriptionID} | Subscription with ID *SubscriptionID* is cancelled |

"{SubscriptionID}" is a placeholder for the identifier of the subscription to be cancelled.
