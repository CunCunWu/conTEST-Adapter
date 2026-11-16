> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Online Analyses

Required Licenses: CTX 000, CTM 020

The recorder in conTEST can be set up to continuously analyze the signal. These analyses can provide single values like the level or be more complex like a FFT. The analyses available through the MQTT adapter are grouped into three types:

| Analysis Type | Description |
| --- | --- |
| 1D | Single Value analyses. E.g., the current level of an airborne signal. |
| 2DEquidistant | Two-dimensional analyses with a fixed abscissa. E.g., the FFT of a signal. |
| 2DBand | Two-dimensional analyses with a floating abscissa. E.g., a running level vs. time. |

The available analyses and updates to the values of the analses are publish on a flexible topic structure. The topics contain the placeholder {analysisType}, which is on of the types in the table above. Updates to the analyses are published on topics containing the placeholder {analysisType} as well as {analysisName}. Thus, you can subscribe to a specific analysis, all analyses of a certain type, or all available analyses using wildcards.

Example topic filter for subscribing to all 1D analyses:

```text
{top-level-topic}/analyses/1D/#
```

## Available Online Analyses

The names of all available analyses of type {analysisType} are published on the topic

```text
{top-level-topic}/analyses/availableAnalyses/{analysisType}
```

The payload is a comma-separated list of the names of available analyses. The names can be defined per analysis within the recorder configuration in conTEST.

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/analyses/availableAnalyses/{analysisType}` | "{Analysis1,Analysis2,Analysis3}" |

## Online Analysis Updates

Updates to all available analyses are published by conTEST continuously on a dedicated topic for each analysis. Subscribe to a specific analysis with this topic pattern:

```text
{top-level-topic}/analyses/{analysisType}/{analysisName}
```

The analysis types are described here. Refer to Available Online Analyses for retrieving available analysis names.

Depending on the analysis type, the payloads published on these topics have different structures:

### 1D Online Analysis

The published payload for a 1D analysis is a comma-separated string with the following structure:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/analyses/1D/{analysisName}` | "{ChannelName},{Value},{Unit}" |

The placeholders are:

| Placeholder | Description |
| --- | --- |
| {ChannelName} | Name of the analyzed channel |
| {Value} | Current value of the analysis |
| {Unit} | Unit of the value |

### 2D Equidistant Analysis

The published payload for a 2D Equidistant analysis is a comma-separated string with the following structure:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/analyses/2DEquidistant/{analysisName}` | "{ChannelName},{Unit},{FirstAbscissaValue},{DeltaAbscissa},{AbscissaUnit},{Values}" |

The placeholders are:

| Placeholder | Description |
| --- | --- |
| {ChannelName} | Name of the analyzed channel |
| {Unit} | Unit of the values |
| {FirstAbscissaValue} | First tick of the abscissa |
| {DeltaAbscissa} | Distance between abscissa ticks |
| {AbscissaUnit} | Unit of the abscissa |
| {Values} | Comma-separated list of current values |

### 2D Band Analysis

The published payload for a 2D Equidistant analysis is a comma-separated string with the following structure:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/analyses/2DEquidistant/{analysisName}` | "{ChannelName},{Unit},{BandType},{FirstAbscissaValue},{LastAbscissaValue},{Values}" |

The placeholders are:

| Placeholder | Description |
| --- | --- |
| {ChannelName} | Name of the analyzed channel |
| {Unit} | Unit of the values |
| {BandType} | Band type; for example "Octave3rd" |
| {FirstAbscissaValue} | First value of the abscissa |
| {LastAbscissaValue} | Last value of the abscissa |
| {Values} | Comma-separated list of current values |
