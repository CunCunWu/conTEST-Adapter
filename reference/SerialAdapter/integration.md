> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Serial Adapter

## Connection Settings

The serial port and baudrate for the connection to conTEST can be specified in the adapter settings. The other settings for the serial connection are fixed:

| Setting | Value |
| --- | --- |
| Data Bits | 8 |
| Parity | None |
| Stop Bits | 1 |

## Message Structure

The first four bytes are reserved for the message type-ID (32-bit integer, little-endian). The following bytes contain the content of the message as an encoded string (Coding: UTF-8, Culture: Invariant (English language)). Messages have to be terminated by the byte value of an asterisk '*'. Responses will also be terminated by an asterisk '*'. Usage of this particular character within messages is prohibited to prevent incorrect detection of message termination.

## Escape Character

Some characters are used by the protocol as separators and therefore must be escaped. Otherwise, the messages cannot be interpreted correctly. Here, backslash ('\') is used as the escape character.

The following characters are reserved and must be escaped:

- Comma ','

- Semicolon ';'

## Quickstart

This section describes how to send a Recording Start command to conTEST. This requires a running conTEST instance with activated licenses CTX 000 and CTM 010. Set up a connection to conTEST with your favorite Serial client. Send the following bytearray to conTEST:

```text
\x01\x00\x00\x00\x53\x74\x61\x72\x74\x2A
```

The first four bytes contain the protocol ID in little-endian encoding, the last five bytes contain the UTF-8 encoded command "Start".

| Field | ID 0 | ID 1 | ID 2 | ID 3 | S | t | a | r | t | * |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hex value | 01 | 00 | 00 | 00 | 53 | 74 | 61 | 72 | 74 | 2A |

An overview over the commands for recorder control is listed here.

## Messages

### Client To Host

| ID | Type |
| --- | --- |
| 1 | Recorder Control |
| 3 | Custom Name |
| 5 | Get Available Profiles |
| 7 | Load Profile |
| 9 | Subscribe To States |
| 11 | Unsubscribe From States |
| 13 | Subscribe To Results |
| 15 | Unsubscribe From Results |
| 17 | Get Processing Variables |
| 19 | Set Processing Variable |
| 21 | Get Available Analyses 1D |
| 23 | Subscribe To Analysis 1D |
| 25 | Get Available Analyses 2D Equidistant |
| 27 | Subscribe To Analysis 2D Equidistant |
| 29 | Get Available Analyses 2D Band |
| 31 | Subscribe To Analysis 2D Band |
| 33 | Unsubscribe From Analysis |
| 35 | Received Analysis 2D Update |
| 37 | Is Postprocessing Licensed |
| 39 | Is Condition Monitoring Licensed |
| 41 | Get Recorder Documentation Attributes |
| 43 | Set Recorder Documentation Attribute Value |
| 45 | Get Available Monitoring Conditions |
| 47 | Subscribe To Condition Monitoring |
| 49 | Unsubscribe From Condition Monitoring |
| 51 | Subscribe To System Events |
| 53 | Unsubscribe From System Events |
| 54 | Set Condition Monitoring Threshold |
| 56 | Set Condition Monitoring ToleranceFile |
| 57 | Live Monitoring Control |
| 61 | Subscribe To Live Monitoring States |
| 63 | Unsubscribe from Live Monitoring States |
| 65 | Get Live Monitoring Status |

### Host To Client

| ID | Type |
| --- | --- |
| 2 | Recorder Control Response |
| 4 | Custom Name Response |
| 6 | Get Abailable Profiles Response |
| 8 | Load Profiles Response |
| 10 | States Updates |
| 14 | New Result |
| 18 | Get Processing Variables Response |
| 20 | Set Processing Variable Response |
| 22 | Get Available Analyses 1D Response |
| 24 | Analysis 1D Update |
| 26 | Get Available Analyses 2D Equidistant Response |
| 28 | Analysis 2D Equidistant Update |
| 30 | Get Available Analyses 2D Band Response |
| 32 | Analysis 2D Band Update |
| 38 | Is Postprocessing Licensed Response |
| 40 | Is Condition Monitoring Licensed Response |
| 42 | Get Recorder Documentation Attributes Response |
| 44 | Set Recorder Documentation Attribute Value |
| 46 | Get Available Monitoring Conditions Response |
| 48 | Condition Monitoring Update |
| 52 | New System Event |
| 55 | Set Condition Monitoring Response |
| 58 | Live Monitoring Control Response |
| 62 | Live Monitoring State Update |
| 66 | Get Live Monitoring Status Response |

## Notation

In this documentation, the contents of the messages are described using placeholder variables. These are marked with curly brackets. Words that are not surrounded by curly brackets are keywords and must be included in exactly the same way as they are specified.
