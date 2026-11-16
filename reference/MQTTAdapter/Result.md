> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Result

Required Licenses: CTX 000, CTM 010

Whenever a new evaluation result is available within conTEST, it is published on the topic

```text
{top-level-topic}/results/latest
```

The result is a comma-separated string containing high-level as well as detailed results:

| Topic | Payload |
| --- | --- |
| `{top-level-topic}/results/latest` | "{ID},{CustomName},{Timestamp},{OverallSuccess},{Classification},{DetailedResults}" |

The elements of the comma-separated list above are:

| Element | Description |
| --- | --- |
| {ID} | ID of the result |
| {CustomName} | User defined custom name or empty |
| {Timestamp} | UTC timestamp |
| {OverallSuccess} | Overall result. One of "OK"/"NOK" |
| {Classification} | Classification based on the evaluation rules of the profile |
| {DetailedResults} | A complete set of information about the recording, processing and evaluation. This is formatted as JSON for easier parsing. |
