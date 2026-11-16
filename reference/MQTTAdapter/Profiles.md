> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Profiles

Required License: CTX 000

conTEST offers the capability to set up various profiles, each with distinct recorder configurations, processing specification and evaluation rules. The name of the currently active profile is published on a dedicated topic. The active profile can also be changed by publishing on a dedicated topic. A list of all available profiles is published on a separate topic.

## Available Profiles

conTEST publishes the names of all available profiles as a comma-separated string on the topic

```text
{top-level-topic}/profiles/availableProfiles
```

An example message is given below

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/profiles/availableProfiles` | "{FirstProfileName},{SecondProfileName},{ThirdProfileName}" |

## Active Profile

The name of the currently active profile is published on the topic

```text
{top-level-topic}/profiles/activeProfile
```

The payload is the name of the active profile:

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/profiles/activeProfile` | "{CurrentlyActiveProfile}" |

## Set Active Profile

conTEST accepts commands to change the active profile on the branch

```text
{top-level-topic}/profiles/setActiveProfile
```

conTEST will try to match the payload to a valid profile name and activate that profile. If the provided name is invalid, the active profile will not change. Please refer to the published list of available profiles to make sure you provide a valid name.

| Topic | Example Payload |
| --- | --- |
| `{top-level-topic}/profiles/setActiveProfile` | "{NewActiveProfile}" |
