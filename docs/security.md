# Security

NeoCatcher works like every HTTPS debugging proxy: it creates a certificate authority (CA) and uses it to decrypt
traffic from clients that trust that CA. That is powerful, so treat the certificate like a password.

## What stays on your machine

- The CA certificate and its private key are generated locally. Keystore passwords are stored in the IDE's
  password safe.
- Captured traffic stays in the IDE's memory. Rules and breakpoints are stored in your project and workspace files.
- NeoCatcher does not send your traffic, telemetry or usage data to us or anyone else.

## Rules for safe use

- **Only intercept traffic you are allowed to.** Your own apps, devices, test accounts and networks.
- **Never install the certificate on a shared or production device.** Anyone with the private key could read that
  device's HTTPS traffic.
- **Don't share the `.jks` / `.p12` files** or commit them to git.
- **Trust user certificates in debug builds only.** Never ship a release build that does.
- **Be careful with what you capture.** The log can contain tokens, cookies and personal data. Clear it when you're
  done, and don't paste it into tickets or chats unredacted.

## AI agents (MCP)

If you enable the [MCP server](mcp.md), AI agents on this computer can read captured traffic:

- It listens on `127.0.0.1` only and requires an access token; **Regenerate token** revokes all clients.
- `Authorization`, `Cookie` and similar header values are redacted unless you choose to reveal them.
- Bodies are not redacted, and what an agent reads goes to its AI provider. Don't capture data you may not share
  with that provider while an agent is connected.
- Agents can change rules and paused responses only after you allow it; every change appears in the Activity log.

## Clean up

When you no longer need NeoCatcher on a device, remove the certificate:

| Where | How to remove |
| --- | --- |
| Android | Settings → Security → Encryption & credentials → User credentials → remove; reset the emulator proxy with `adb shell settings put global http_proxy :0` |
| JVM | `keytool -delete -alias <alias> -cacerts` |
| macOS | Keychain Access → System → delete the certificate |
| Windows | `certmgr.msc` → Trusted Root Certification Authorities → delete |
| iOS | Settings → General → VPN & Device Management → remove the profile |

Then delete the certificate files from the folder you generated them in.

## Reporting a vulnerability

Email [security@neocatcher.com](mailto:security@neocatcher.com). Please don't open a public issue.
