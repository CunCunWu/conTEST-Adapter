> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Outputs

Please note that all outputs are implemented as "active high".

This page describes the functionality of all outputs, please refer to Overview to maps these outputs to physical outputs for your device.

## System States

#### General System Status

Indicates that the system is ready and not in an error state.

#### Recording Running

Indicates that a recording is currently in progress.

#### Processing Running

Indicates that a completed recording is being processed.

#### Evaluation Running

Indicates that the results of a processed recording are currently evaluated.

## Test Result

When a new test result is available, an indiator output at "Result Ready" is turned on. A signal indicating the test results outcome is applied to one of the outputs at "OK", "NOK" or "Error". This requires the licences CTX 000 and CTM 010.

#### Result Ready

Indicator Pin for availability of new test result. Is turned off just before a new test result becomes available and turned on just after the new test result is available.

#### OK

Indicates an OK test result.

#### NOK

Indicates an NOK test result.

#### Error

Indicates that an error occured during processing.

## Condition Monitoring

This requires the licences CTX 000 and CTM 020.

#### OK

If there are available conditions and all conditions are within bounds, the output is active.

#### NOK

If there are available conditions and at least one of the conditions is out of bounds, the output is active.
