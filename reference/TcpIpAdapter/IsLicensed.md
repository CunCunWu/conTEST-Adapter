> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# License Query

Required License: CTX 000

## CTM 010 conTEST Postprocessing

### Is Postprocessing Licensed

The client can use the following message to inquire whether conTEST Postprocessing (CTM 010) is licensed or not:

| ID | Content | Response |
| --- | --- | --- |
| 37 |  | *Is Postprocessing Licensed Response* (ID:38) |

The content of this message has to be empty. The host will respond with *Is Postprocessing Licensed Response* (ID:38).

### Is Postprocessing Licensed Response

Upon receipt of the *Is Postprocessing Licensed* message, the host sends the subsequent message:

| ID | Content (CTM 010 Licensed) | Content (CTM 010 Not Licensed) |
| --- | --- | --- |
| 38 | True | False |

## CTM 020 conTEST Condition Monitoring

### Is Condition Monitoring Licensed

The client can use the following message to inquire whether conTEST Condition Monitoring (CTM 020) is licensed or not:

| ID | Content | Response |
| --- | --- | --- |
| 39 |  | *Is Condition Monitoring Licensed Response* (ID:40) |

The content of this message has to be empty. The host will respond with *Is Condition Monitoring Licensed Response* (ID:40).

### Is Condition Monitoring Licensed Response

Upon receipt of the *Is Condition Monitoring Licensed* message, the host sends the subsequent message:

| ID | Content (CTM 020 Licensed) | Content (CTM 020 Not Licensed) |
| --- | --- | --- |
| 40 | True | False |
