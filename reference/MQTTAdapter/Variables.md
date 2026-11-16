> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Variables

Required Licenses: CTX 000, CTM 010

Variables can be used in the processing segment to fine-tune analyses. You can define variables in the processing specifications within conTEST. The names of available variables are published on a dedicated topic given below. Available variables can be set to a custom value through a separate topic also given below.

## Available Processing Variables

The names of all available variables to be set are published on the topic

```text
{top-level-topic}/variables/availableVariables
```

The published payload is a comma-separated string listing the names of the available variables.

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/variables/availableVariables` | "{FirstVariable},{SecondVariable},{ThirdVariable}" |

## Set Processing Variable

You can provide a new value for an available variable on the topic

```text
{top-level-topic}/variables/setVariable
```

The required payload is a string with comma-separated variable name and new value.

Example message setting the value of "SecondVariable" to "NewValue": |Topic|Example Payload| |----|-----| |`{top-level-topic}/variables/setVariable`|"SecondVariable,NewValue"|

Upon receiving a message on this topic, conTEST will try to match the variable name to an available variable and update its value. You will not receive a notification of whether this operation has succeeded.
