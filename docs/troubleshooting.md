# Troubleshooting

## Nothing shows up in the Request Log

- Is the proxy running? The **Server** tab shows its status; click **Refresh**.
- Is the client really using the proxy? Test with
  `curl --proxy http://localhost:9942 http://example.com`.
- Android emulator: the proxy host is `10.0.2.2`, not `localhost`.
- Physical device: use your computer's LAN IP, and check that your firewall allows incoming connections on the port.
- A VPN on the computer or device can bypass or block the proxy. Turn it off while debugging.
- HTTPS calls are missing but plain HTTP shows up? **Decrypt HTTPS** is off in the Server tab; HTTPS then passes
  through unseen.

## Certificate errors (SSL handshake failed, unknown CA)

- The client doesn't trust the NeoCatcher certificate. Install the `.cer` file for that client: see
  [Device setup](device-setup.md).
- Android: your app also needs the debug network security config that trusts **user** certificates.
- JVM: the app must run on the same JDK whose truststore you imported into.
- Regenerated the certificate? Install the new one everywhere; the old one no longer matches.
- A release build that must not trust the certificate: turn off **Decrypt HTTPS** in the Server tab, see
  [Release builds](device-setup.md#release-builds).

## Only some HTTPS requests fail

The app probably uses **certificate pinning** (for example OkHttp `CertificatePinner`), which rejects any
certificate except the real server's. Disable pinning in debug builds.

## I can't start the Pro trial (Android Studio)

Android Studio needs the **JetBrains Marketplace Licensing** plugin for paid plugins. Install it from
**Settings → Plugins → Marketplace** (the Pro notification's **Open Plugins Settings…** takes you there), restart,
then **Get Pro…** in the Server tab or **Help → Manage Licenses…**. See
[Trial and purchase](trial-and-purchase.md).

## "Could not root your Android Emulator"

The emulator uses a **Google Play** system image. Create one with a **Google APIs** image instead.

## Port already in use

Another program uses `9942`. Change the port in the **Server** tab, click **Restart**, and update your clients.

## A paused response never arrives

Check the **Breakpoints** tab — the response is waiting for you. Paused responses continue on their own after
10 minutes.

## My AI agent cannot reach NeoCatcher

See [AI agents → Troubleshooting](mcp.md#troubleshooting).

## Still stuck?

Email [support@neocatcher.com](mailto:support@neocatcher.com) with your IDE version, NeoCatcher version, the client
(emulator, JVM, browser) and what you see. Never send real passwords or tokens.
