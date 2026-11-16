> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Get Available Profiles

Required License: CTX 000

conTEST offers the capability to set up various profiles, each with distinct recorder configurations, processing specification and evaluation rules. The active profile can be changed using this network interface. Initially, the client has the option to inquire about the available profiles (refer to the details below). Subsequently, the client can change the active profile by loading the preferred profile using its corresponding name (refer to Load Profile).

## Get Available Profiles

The following message requests a list of all available profiles:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 5 |  | * | *Get Available Profiles Response* (ID:6) |

The content of this specific message has to be empty. The host will respond with *Get Available Profiles Response* (ID:6).

## Get Available Profiles Response

Upon receipt of the *Get Available Profiles* message, the host sends the subsequent message containing a list of the available profiles:

| ID | Content | Terminator | Example |
| --- | --- | --- | --- |
| 6 | {List of names of profiles seperated by comma (',')} | * | Profile 1,Profile 2, Profile 3* |

The names of the profiles can be used to set the active profile (refer to Load Profile)
