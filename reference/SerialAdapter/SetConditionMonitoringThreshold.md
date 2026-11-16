> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Set Condition Monitoring Option

Required Licenses: CTX 000, CTM 020

When Condition Monitoring is configured in conTEST, clients can update the tolerances underlying the condition.

The client can initially inquire about the available conditions (refer to Get Available Monitoring Conditions). Subsequently, the client can modify the underlying tolerance by sending a corresponding message containing the ID of the condition and new tolerance options (refer to the details below).

## Set Condition Monitoring Threshold

The client can modify the underlying threshold of a 1D condition by sending the following message:

| ID | Content |
| --- | --- |
| 54 | {ConditionID},{Threshold} |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{ConditionID}|ID of the targeted condition| |{Threshold}|New value for the threshold|

After the host receives the subscription request, it sends a *Set Condition Monitoring Response* message (see below).

## Set Condition Monitoring ToleranceFile

The client can modify the underlying tolerance file for a condition based on a 2D analysis by sending the following message:

| ID | Content |
| --- | --- |
| 56 | {ConditionID},{ToleranceFilePath},{LowerCurveID},{UpperCurveID} |

Explanation of placeholders: |Placeholder|Explanation| |-|-| |{ConditionID}|ID of the targeted condition| |{ToleranceFilePath}|Path to the new tolerance file| |{LowerCurveID}|String identifier for the lower tolerance curve| |{UpperCurveID}|String identifier for the upper tolerance curve|

After the host receives the subscription request, it sends a *Set Condition Monitoring Response* message (see below).

## Set Condition Monitoring Response

Upon receiving a *Set Condition Monitoring Threshold* or *Set Condition Monitoring ToleranceFile* message, the host sends back a message to the client indicating whether the message has been successfully received and processed

| ID | Content | Description |
| --- | --- | --- |
| 55 | "True"/"False" | Indication of whether the operation was successful |
