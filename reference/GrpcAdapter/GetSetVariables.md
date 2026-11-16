> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

## GetVeriables and SetVariable

The used processing specification (hpsx) may contain processing variables for fine tuning an evaluation. By calling *GetVariables* a list of available processing variable names is returned. These names can be used to identify a processing variable when calling *SetVariable* with respective *name* and *value*.

- GetVariables

- SetVariable

```text
rpc GetVariables(GetVariablesRequest) returns (GetVariablesReply);

message GetVariablesRequest {
}

message GetVariablesReply {
    repeated string variables = 1;
}
```

```text
rpc SetVariable(SetVariableRequest) returns (SetVariableReply);

message SetVariableRequest {
    string name = 1;
    string value = 2;
}

message SetVariableReply {
}
```
