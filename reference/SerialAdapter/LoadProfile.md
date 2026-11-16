> Extracted from the locally installed conTEST 1.15 Adapter help. See [source policy](../../docs/source-and-version.md).

# Load Profile

Required License: CTX 000

conTEST offers the capability to set up various profiles, each with distinct recorder configurations, processing specification and evaluation rules. The active profile can be changed using this network interface. Initially, the client has the option to inquire about the available profiles (refer to Get Available Profiles). Subsequently, the client can change the active profile by loading the preferred profile using its corresponding name (refer to the details below).

## Load Profile

The client can request the loading of a specific profile with the following message:

| ID | Content | Terminator | Response |
| --- | --- | --- | --- |
| 7 | {ProfileName} | * | *Load Profile Response* (ID:8) |

"{ProfileName}" is a placeholder for the name of the desired profile. For example, the content of the message could look like this: "Profile 1".

As indication to the client that the host has successfully received and processed the message, the host will issue the response *Load Profile Response* (ID:8).

## Load Profile Response

When the *Load profile* message is received, the host sends the following message to the client, indicating whether the request to load the desired profile was successful:

| ID | Content (Request Successful) | Content (Request Failed) | Terminator |
| --- | --- | --- | --- |
| 8 | True | False | * |
