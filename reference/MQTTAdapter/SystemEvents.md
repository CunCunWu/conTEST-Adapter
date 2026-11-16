> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# System Events

Required License: CTX 000

System events of conTEST are published on dedicated topics. Subscribe to these topics to be continuously informed. The events received are identical to those displayed on the dashboard in the events content. They are published on topics reflecting their severity:

| Event Severity | Topic |
| --- | --- |
| Info | `{top-level-topic}/systemEvents/Info` |
| Warning | `{top-level-topic}/systemEvents/Warning` |
| Error | `{top-level-topic}/systemEvents/Error` |

You can subscribe to these topics individually, or use a wildcard to subscribe to all event severities:

```text
{top-level-topic}/systemEvents/#
```

The published payloads contains a UTC timestamp, the source of the message, and the message itself separated by comma:

| Example Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/systemEvents/{Info/Warning/Error}` | "{Timestamp},{Source},{Message}" |
