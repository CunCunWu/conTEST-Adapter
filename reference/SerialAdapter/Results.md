> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Subscribe To Results

Required Licenses: CTX 000, CTM 010

After each record, conTEST automatically processes the recording and performs an evaluation according to a configured rule set. The client can subscribe to be continuously informed about new results.

## Subscribe To Results

The client can start the subscription with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 13 | {SubscriptionID} | * | Subscription is started and results are sent to client with *New Result* messages (ID:14) |

"{SubscriptionID}" is a placeholder for the identifier of the subscription, which has to be unique regarding all subscriptions and is issued by the client.

Once the host receives the subscription request, subsequently new results are sent to the client in the form of *New Result* messages.

## New Result

If a subscription is established, every time a new result is available, the host sends the following message to the client:

| ID | Content | Terminator |
| --- | --- | --- |
| 14 | {ID},{CustomName},{Timestamp},[OK/NOK],{Classification},{Details in JSON format} | * |

Explanation of placeholders:

| Placeholder | Explanation |
| --- | --- |
| {ID} | ID of the result |
| {CustomName} | User defined custom name or empty |
| {Timestamp} | UTC timestamp |
| [OK/NOK] | Overall result. Is either "OK" or "NOK" |
| {Classification} | Classification based on the evaluation rules of the profile |
| {Details in JSON format} | A complete set of information about the recording, processing and evaluation. This is formatted as JSON for easier parsing. |

## Unsubscribe From Results

The client can unsubscribe from new result updates with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 15 | {SubscriptionID} | * | Subscription with ID *SubscriptionID* is cancelled |

"{SubscriptionID}" is a placeholder for the identifier of the subscription to be cancelled.
