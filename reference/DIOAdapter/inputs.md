> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Inputs

Please note that all inputs are implemented as "active low" and are polled within a timespan that can be set in the adapter settings.

This page describes the functionality of all inputs, please refer to Overview to maps these inputs to physical inputs for your device.

## Recording Control

This requires the licence CTX 000.

#### Start Recording

A recording can be started by applying a signal to the channel mapped to "Start Recording". If a recording is already in progress, conTEST will disregard any subsequent start commands, as it is designed to handle only one recording at a time. As indication that a recording is in progress a signal is outputted at "Recording Running" (refer to Outputs).

#### Stop Recording

To stop the recording a signal has to be applied to the channel mapped to "Stop Recording". If no recording is currently in progress, conTEST will desregard the command. As soon as the recording has stopped, processing and evaluation are automatically executed. This is also indicated by the system states outputs (refer to Outputs).

A signal that is simultaneously applied to both "Start Recording" and "Stop Recording" is going to be ignored.

## Condition Monitoring

This requires the licences CTX 000 and CTM 020.

#### Acknowledge Condition Monitoring Out Of Bounds

If the option "Require acknowledgement of condition monitoring NOK" is set in the DIO Adapter settings within conTEST, the status of the Condition Monitoring Output will not change from NOK to OK whenever the limits changes from "out of bounds" to "within bounds". Hold this input for a time greater than the polling time configured in the adapter settings to enable the change from NOK to OK. You can also hold this input to prevent the status of the Condition Monitoring Output to change from OK to NOK.
