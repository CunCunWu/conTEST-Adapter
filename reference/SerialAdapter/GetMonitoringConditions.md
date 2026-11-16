> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Monitoring Conditions

Required Licenses: CTX 000, CTM 020

When Condition Monitoring is configured in conTEST, clients can subscribe to receive continuous updates on whether the condition is met or not.

The client can initially inquire about the available conditions (refer to the details below). Subsequently, the client can start the subscription by sending the corresponding message containing the ID of the condition (refer to Subscribe To Condition Monitoring).

## Get Available Monitoring Conditions

The client can request a list of the available conditions with the following message:

| ID | Content | Response |
| --- | --- | --- |
| 45 |  | *Get Available Monitoring Conditions Response* (ID:46) |

The content of this message has to be empty. The host will respond with *Get Available Monitoring Conditions Response* (ID:46).

## Get Available Monitoring Conditions Response

When the *Get Available Monitoring Conditions* message is received, the host sends the subsequent message containing a list of the available conditions:

| ID | Content | Example |
| --- | --- | --- |
| 46 | {List of condition information ({ID};{Description};{ToleranceType};{ToleranceOptions}) separated by comma (',')} | ID1;Level.Exceeds80dB;ThresholdBased;-0.4,ID2;FFT.Optimal;ToleranceFileBased;C:\Users\myUser\Tolerance.htsx;lowerCurve;upperCurve |

In the content of the message, each condition is seperated by a comma (','). In the given example, the substring containing the information of the first condition is "ID1;Level.Exceeds80dB;ThresholdBased;-0.4". This represents a tuple consisting of the ID "ID1", the description "Level.Exceeds80dB", the tolerance type "ThresholdBased", and the threshold value "-0.4". The parts are seperated by a semicolon (';'). The description itself contains the analysis name "Level" and the user defined identifier of the limit "Exceeds80dB", which are seperated by a point ('.'). The second condition is based on a 2D analysis (here: FFT). The {ToleranceOptions} consist of a path to a tolerance file, and string identifiers for the lower and upper curve. They are separated by a semicolon (';').

The ID of a condition can be used to start the subscription (refer to Subscribe To Condition Monitoring).
