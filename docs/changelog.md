# Changelog

## 1.0.2 — 2026-10-27

### Added

- Response rules can take the body from a file in your project (like Map Local). The file is read on every
  response, so edits show up on the next request, and the path is stored relative to the project.
  See [Rules](rules.md#serve-a-response-from-a-file-in-your-project).
- Response rules can delay the response by up to 60 seconds to test slow networks, loading states and timeouts.
- **Decrypt HTTPS** switch on the Server tab. Turn it off and HTTPS goes straight to the server, so builds that don't
  trust the NeoCatcher certificate (release builds) keep working; plain HTTP is still shown and changed by rules.
  No restart needed. See [Release builds](device-setup.md#release-builds).
- Apps that prefer HTTP/2 keep it through the proxy, and rules still apply to their calls.
- In IDEs without built-in license checks, such as Android Studio, the Pro notification points to JetBrains
  Marketplace Licensing, which the free trial and purchase need, and opens the Plugins settings to install it.
  See [Trial and purchase](trial-and-purchase.md).

### Changed

- New rule conditions compare with Glob instead of Equals: a plain value still matches exactly, and `*` is there
  when you need it.
- Connect wizard: steps you shouldn't skip move on with **Next**; only optional steps offer **Skip**.
- Supported IDEs: 2025.3 up to the current EAP (2026.3). Later IDE versions are added in later releases, once tested.

### Security

- The proxy port no longer gives access to the proxy engine's own API: it refuses everyone but NeoCatcher itself, so
  devices on your network can't add mock responses or read captured traffic through it. The engine's built-in MCP
  endpoint and dashboard analytics are turned off.

## 1.0.1 — 2026-10-21

- Consistent NeoCatcher name in menu actions, dialogs, notifications and rule schemas.
- New certificates are issued as "NeoCatcher CA" and saved as `neocatcher-cert` by default. Certificates created
  earlier keep working under their old names.

## 1.0.0 — 2026-10-17

First public release.

- Local HTTP(S) proxy with CA certificate generation
- Connect wizard for Android emulators and phones, Java/Kotlin apps, browsers, this computer, iOS and terminals
- Server tab with clients, certificate status, traffic and an activity log
- Request log with formatted bodies, diff and Copy as cURL
- Request and response rules with a visual, YAML and JSON editor
- Response breakpoints: pause, edit, send or abort
- MCP server for AI agents: read captured traffic; optionally create rules and resume paused responses
