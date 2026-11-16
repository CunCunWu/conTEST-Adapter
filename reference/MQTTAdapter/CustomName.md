> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Custom Name

Required License: CTX 000

The custom name serves an optional additional identifier for the recording/result. For instance, it could be the serial number of the device being tested. Once the custom name is set, it will be attached as an attribute to all subsequent recordings/results until a new custom name is set.

## Set Custom Name

To set a custom name, publish the desired name on the topic

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/customName/setCustomName` | {NewCustomName} |
