> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Licenses

Required License: CTX 000

The status of activated licences is published on `{top-level-topic}/licences/{licenseName}`. The payload message is one of two strings indicating whether the license is active or not. The messages published by conTEST on these topics are retained by the broker.

## Post Processing Licence CTM 010

The activation status of CTM 010 conTEST Postprocessing is published on

```text
{top-level-topic}/licences/postProcessing
```

The content of the message is:

| Content (CTM 010 Licensed) | Content (CTM 010 Not Licensed) |
| --- | --- |
| "True" | "False" |

## Condition Monitoring Licence CTM 020

The activation status of CTM 020 conTEST Condition Monitoring is published on

```text
{top-level-topic}/licences/conditionMonitoring
```

The content of the message is:

| Content (CTM 020 Licensed) | Content (CTM 020 Not Licensed) |
| --- | --- |
| "True" | "False" |
