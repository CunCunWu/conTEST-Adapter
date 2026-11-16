> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Recorder Control

Required Licenses: CTX 000

The recorder within conTEST can be started and stopped remotely. conTEST accepts commands for recorder control on the topic

```text
{top-level-topic}/recorder/control
```

## Starting a recording

To start the recorder, publish the payload "Start" on the recorder control topic:

| Topic | Start Payload |
| --- | --- |
| `{top-level-topic}/recorder/control` | "Start" |

## Stopping a recording

To stop the recorder, publish the payload "Stop" on the recorder control topic:

| Topic | Start Payload |
| --- | --- |
| `{top-level-topic}/recorder/control` | "Stop" |
