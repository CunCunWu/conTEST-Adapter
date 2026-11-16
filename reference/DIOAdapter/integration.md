> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Digital I/O Adapter

With the Digital I/O Adapter the client can control conTEST over a USB connected Digital I/O device. As a result of the simple interface, only a restricted set of functionalities are accessible, as outlined below.

## Requirements

The license CTX 100 is required for remoting. A digital I/O device must be connected to the computer that is running conTEST. At the moment, two devices by vendor Advantech are supported:

- USB-5750

- USB-5855

The device to be used can be selected in the Adapter settings within conTEST. The device type must be included in the Device Description. (Default by Manufacturer)

## Notation

The channels are denoted in the way they are marked on the DIO device.

## Channel Overview

- Advantech USB-4750

- Advantech USB-5855

Please refer to the manufacturer manuals for how to connect to inputs and outputs.

#### Input Channels

All Inputs are treated as active low.

| Channel | Function |
| --- | --- |
| IDI1 | Start Recording |
| IDI2 | Stop Recording |
| IDI9 | Acknowledge Condition Monitoring Out Of Bounds |

For a detailed description refer to Inputs.

#### Output Channels

All Outputs are treated as active high.

| Channel | Function |
| --- | --- |
| IDO0 | General System Status |
| IDO1 | Recording Status |
| IDO2 | Processing Status |
| IDO3 | Evaluation Status |
| IDO4 | Result Ready Flag |
| IDO8 | Test OK |
| IDO9 | Test NOK |
| IDO10 | Test Error |
| IDO11 | Condition Monitoring OK |
| IDO12 | Condition Monitoring NOK |

For a detailed description refer to Outputs.

Please refer to the manufacturer manuals for how to connect to inputs and outputs.

#### Input Channels

All Inputs are treated as active low.

| Channel | Function |
| --- | --- |
| I1 | Start Recording |
| I2 | Stop Recording |
| I9 | Acknowledge Condition Monitoring Out Of Bounds |

For a detailed description refer to Inputs.

#### Output Channels

All Outputs are treated as active high.

| Channel | Function |
| --- | --- |
| C + NO 0 | General System Status |
| C + NO 1 | Recording Status |
| C + NO 2 | Processing Status |
| C + NO 3 | Evaluation Status |
| C + NO 4 | Result Ready Flag |
| C + NO 8 | Test OK |
| C + NO 9 | Test NOK |
| C + NO 10 | Test Error |
| C + NO 11 | Condition Monitoring OK |
| C + NO 12 | Condition Monitoring NOK |

For a detailed description refer to Outputs.
