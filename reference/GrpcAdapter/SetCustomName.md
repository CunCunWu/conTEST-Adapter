> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## SetCustomName

Sets a custom name for future identification of current records by calling this procedure with *customName* of your choice.

- SetCustomName

```text
rpc SetCustomName(CustomNameRequest) returns (CustomNameReply);

message CustomNameRequest {
    string customName = 1;
}

message CustomNameReply {

}
```
