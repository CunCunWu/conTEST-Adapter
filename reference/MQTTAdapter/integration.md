> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# MQTT Adapter

## Connection to MQTT broker

The MQTT Adapter needs to connect to an external MQTT broker (server) to publish and receive messages. Specify the IP address and port the broker is accepting connections on in the settings page.

## Top level topic

The MQTT Adapter publishes and receives messages on topics relative to the top level topic specified in the adapter settings. All topics are described here. This enables you to provide custom names for each conTEST instance in your environment. E.g., you could give two machines the top level topics

- conTEST/machine1/

- conTEST/machine2/

and subscribe to all relevant topics with a single wildcard, e.g. conTEST/+/... .

## Quickstart

Connect to your MQTT broker and subscribe to the topic

`{top-level-topic}/state/#`.

You will receive messages for the states for recording, analysis, and evaluation. A detailed explanation is given here.

## Topics and Messages

### Control Topics

These are the topics conTEST subscribes to in order to recieve commands. Publish commands on these topics to control the behavior of conTEST.

| Topic | Description |
| --- | --- |
| `{top-level-topic}/recorder/control` | Recorder Control |
| `{top-level-topic}/customName/setCustomName` | Set Custom Name |
| `{top-level-topic}/profiles/setActiveProfile` | Set Active Profile |
| `{top-level-topic}/variables/setVariable` | Set Processing Variable |
| `{top-level-topic}/documentation/setAttribute` | Set Documentation Attribute |
| `{top-level-topic}/conditions/setCondition` | Set Condition Tolerance |
| `{top-level-topic}/liveMonitoring/control` | Live Monitoring Control |

### Published Topics

These are the topics conTEST publishes information on. Subscribe to these topics to receive that information.

| Topic | Description |
| --- | --- |
| `{top-level-topic}/profiles/availableProfiles` | Available Profiles |
| `{top-level-topic}/profiles/activeProfile` | Active Profile |
| `{top-level-topic}/state/recorder` | Recorder State |
| `{top-level-topic}/state/analysis` | Analysis State |
| `{top-level-topic}/state/evaluation` | Evaluation State |
| `{top-level-topic}/results/latest` | Result |
| `{top-level-topic}/variables/availableVariables` | Available Processing Variables |
| `{top-level-topic}/analyses/availableAnalyses/{analysisType}` | Available Online Analyses |
| `{top-level-topic}/analyses/{analysisType}/{analysisName}` | Online Analysis Updates |
| `{top-level-topic}/conditions/availableConditions` | Available Monitoring Conditions |
| `{top-level-topic}/conditions/{conditionId}` | Monitoring Condition Updates |
| `{top-level-topic}/licences/postProcessing` | Post Processing Licence |
| `{top-level-topic}/licences/conditionMonitoring` | Condition Monitoring Licence |
| `{top-level-topic}/documentation/availableAttributes` | Available Documentation Attributes |
| `{top-level-topic}/systemEvents/{eventSeverity}` | System Events |
| `{top-level-topic}/liveMonitoring/state` | Live Monitoring State |

### Retained Messages

All messages published by conTEST are flagged to be retained at the broker. This allows a client connecting to the broker when conTEST is already running to receive messages sent by conTEST beforehand.

## Notation

In this documentation, the contents of the messages and topics are described using placeholder variables. These are marked with curly brackets. Words that are not surrounded by curly brackets are keywords and must be included in exactly the same way as they are specified.
