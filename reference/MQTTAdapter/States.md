> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# States

Required License: CTX 000

The current status of the three main components of conTEST is published on dedicated topics. You can use these statuses to monitor conTEST remotely, simply subscribe to the topics given below. If you want to monitor all states simultaneously, subscribe to all topics with a wildcard:

```text
{top-level-topic}/state/#
```

## Recorder State

The recorder is responsible for measuring data within conTEST. Its state is published on the branch

```text
{top-level-topic}/state/recorder
```

The published payload is a string indicating the status of the recorder; it takes one of these values:

| Payload | Description |
| --- | --- |
| Disabled | The recorder is unable to start a measurement |
| Idle | The recorder is ready to start a measurement |
| Running | The recorder is taking a measurement or is waiting for triggers |

## Analysis State

The analysis segment of conTEST runs the analyses specified in the processing specification. Its state is published on the branch

```text
{top-level-topic}/state/analysis
```

The published payload is a string indicating the status of the analysis segment; it takes one of these values:

| Payload | Description |
| --- | --- |
| Disabled | The analysis segment is unable to run |
| Idle | The analysis segment is waiting for data from the recorder |
| Running | The analysis segment is currently running |

## Evaluation State

The evaluation segment of conTEST produces the OK/NOK criterion and classifies the results of the analysis segement. Its state is published on the branch

```text
{top-level-topic}/state/evaluation
```

The published payload is a string indicating the status of the evaluation segment; it takes one of these values:

| Payload | Description |
| --- | --- |
| Disabled | The evaluation segment is unable to run |
| Idle | The evaluation segment is waiting for data from the analysis segment |
| Running | The evaluation segment is currently running |
