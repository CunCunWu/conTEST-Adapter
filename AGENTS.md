# Agent Instructions

This repository is an interface knowledge base for the **conTEST 1.15 ContinuousTesting Adapter**. Follow these rules when answering questions or implementing integrations.

## Required reading order

1. Read `docs/adapter-selection.md` if the transport is not already fixed.
2. Read `docs/capability-index.md` and follow the link for the requested capability.
3. Read the selected adapter's `reference/<Adapter>/integration.md`.
4. Read every linked operation page used by the implementation. Do not implement from the overview table alone.
5. For gRPC, treat `protocol/grpc/CtGrpcRemote.proto` as the 1.15 wire contract.

## Hard constraints

- Scope all claims to conTEST 1.15 unless a newer installed help set has been inspected.
- Never invent an IP address, TCP/gRPC port, COM port, baudrate, MQTT broker credential, top-level topic, profile name, analysis name, variable name, documentation attribute identifier, or condition ID. Obtain it from the target conTEST settings or discovery call/topic.
- Check the exact page's `Required License` or `Required Licenses` before promising availability. License presence and feature configuration are separate checks.
- Preserve case, separators, enum spelling, message IDs, field numbers, and payload keywords exactly as documented.
- TCP/IP and Serial IDs are 32-bit little-endian. Encode content as UTF-8 with invariant/English formatting. Escape `,` and `;` as `\,` and `\;` in protocol text.
- Serial frames end with byte `0x2A` (`*`); `*` is prohibited inside message content. TCP/IP frames do not use this terminator.
- MQTT messages published by conTEST are retained. A newly connected client may receive an old retained state immediately; use application timestamps/state transitions where available and do not treat connection-time receipt alone as a new test event.
- For streaming/subscription APIs, plan cancellation/reconnection and idempotent handling. Use a stable unique subscription `id` where the contract provides one.
- Never infer undocumented success acknowledgement. Some operations explicitly have no success notification; report that limitation to callers.
- Do not claim runtime verification unless a real conTEST instance and required licenses were exercised.

## Known documentation gaps

- Live Monitoring appears in TOCs/overviews, but several standalone pages are absent from the installed 1.15 help directory used here. gRPC is fully described by the extracted proto. For TCP/IP, Serial, and MQTT, do not invent the missing payload details; verify against the target installation or capture real traffic.
- The Digital I/O overview contains a `USB-5750` versus `USB-4750` model-name inconsistency. Treat the physical device identity and wiring as unverified until checked in conTEST and the manufacturer manual.

## Implementation checklist

- Record the target conTEST version and chosen adapter.
- Record required licenses and observed license status.
- Keep connection settings in configuration/environment, never source code.
- Implement framing and incremental reads; do not assume one socket/serial read equals one logical message.
- Add tests for non-ASCII UTF-8 and escaped comma/semicolon values where the relevant message accepts text.
- Handle disconnected/restarted conTEST and duplicate/retained events.
- Link implementation comments to the exact `reference/` page used.
