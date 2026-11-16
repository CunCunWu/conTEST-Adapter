> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Recorder Control

Required Licenses: CTX 000

With the recorder control message the client can start and stop recordings. After stopping a recording the processing chain is automatically triggered.

## Start Recording

The client can use the following message to initiate a request, which will trigger the start of a recording:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 1 | Start | * | *Recorder Control Response* (ID:2) |

As indication to the client that the host has successfully received and processed the message, the host will issue the response *Recorder Control Response* (ID:2). If a recording is already in progress, the host will disregard any subsequent start commands, as it is designed to handle only one recording at a time. However, a response will still be sent.

## Stop Recording

The client can use the following message to initiate a request, which will trigger the stopping of a recording:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 1 | Stop | * | *Recorder Control Response* (ID:2) |

In order to signal to the client that the host has successfully received and processed the message, the host will issue the response *Recorder Control Response* (ID:2). If no recording is currently in progress, the host will desregard the command. However, a response will still be sent.

As soon as the recording has stopped, processing and evaluation are automatically executed. Should the client opt for subscribing to updates on results (refer to Subscribe To Results), they will be notified with the new result message.

## Recorder Control Response

Upon receipt of a recorder control command, the host sends the subsequent message as an indication to the client that the command has been successfully received and processed:

| ID | Content | Terminator |
| --- | --- | --- |
| 2 | True | * |
