> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Condition Monitoring

Required Licenses: CTX 000, CTM 020

conTEST allows you to set Limits on online Analyses. These limits are also sometimes called monitoring conditions. These status of these conditions (within bounds or out of bounds) is published on dedicated topics by the MQTT adapter. You can also adjust and exchange the limits set on the analyses on a dedicated topic through the MQTT Adapter.

## Available Monitoring Conditions

Each condition is identified by an ID and has an associated description, tolerance type, and tolerance setting. The ID is a unique string (GUID). The description is a composite of the name of the underlying analysis and the Identifier of the Limit. The tolerance type is one of two depending on the dimensionality of the underlying analysis:

| Tolerance Type | Description |
| --- | --- |
| "ThresholdBased" | The condition is based on a 1D analysis (e.g. a level) |
| "ToleranceFileBased" | The condition is based on a 2D analysis (e.g) an FFT |

The tolerance setting depends on the tolerance type. In case of a "ThresholdBased" condition, the tolerance setting is a string encoding a floating point number encoding the threshold. In case of a "ToleranceFileBased" condition, the tolerance setting is composed of three strings: A path to a tolerance file, a string identifier for the lower curve within the tolerance file, and a string identifier for the upper curve in the tolerance file. In case of an unspecified setting, the strings are empty.

The IDs, short descriptions, tolerance types, and tolerances of all available conditions are published on the topic

```text
{top-level-topic}/conditions/availableConditions
```

The payload sent on this topic is a comma-separated string containing the aforementioned fields for each available condition:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/conditions/availableConditions` | "{ID1};{AnalysisName1}.{LimitIdentifier1};{"ThresholdBased"};{ToleranceSetting},{ID2};{AnalysisName2}.{LimitIdentifier2};{"ToleranceFileBased"};{ToleranceFilePath};{LowerCurve};{UpperCurve}" |

## Monitoring Condition Updates

Updates on monitoring conditions are issued whenever there is a change in the condition status. The condition can either be within bounds or out of bounds. Updates to monitoring conditions are published on a dedicated topic for each condition indicated by their ID. To retrieve the avalivable IDs, refer to Available Monitoring Conditions.

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/conditions/{ID}` | "{True/False}" |

The payload of an update message indicates whether the condition is within bounds:

| Condition Monitoring Update Payload | Description |
| --- | --- |
| "True" | The condition is within bounds |
| "False" | The condition is out of bounds |

## Set Condition Tolerance

All conditions have an underlying tolerance. You can exchange the underlying tolerance for all available conditions by publishing a string containing the new settings on the topic

```text
{top-level-topic}/conditions/setCondition
```

Depending on the ToleranceType (see Available Monitoring Conditions) of the targeted condition, conTEST expects different messages:

| Tolerance Type | Expected Message |
| --- | --- |
| "ThresholdBased" | {ID},{NewThresholdValue} |
| "ToleranceFileBased" | {ID},{NewToleranceFilePath},{NewLowerCurve},{NewUpperCurve} |

Here, {ID} denotes the ID of the targeted condition (see Available Monitoring Conditions).

No confirmation of the setting is published by the MQTT Adapter.
