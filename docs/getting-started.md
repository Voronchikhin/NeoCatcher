# Getting started

From zero to your first captured HTTPS request in about five minutes.

## 1. Install the plugin

1. Open **Settings → Plugins → Marketplace**.
2. Search for **NeoCatcher** and click **Install**.
3. Restart the IDE if asked.

Works in IntelliJ IDEA, Android Studio and other JetBrains IDEs, version 2023.2 or newer.

## 2. Open the tool window

Open **View → Tool Windows → NeoCatcher**. It docks at the bottom and has these tabs:

| Tab | What it's for |
| --- | --- |
| Server | Start and stop the proxy, set the port, manage the certificate |
| Request Log | Every captured request and response |
| Breakpoints | Paused responses and breakpoint rules |
| Request Mappings | Rules that change requests |
| Response Mappings | Rules that change responses |

## 3. Create the CA certificate

HTTPS traffic can only be read if your client trusts NeoCatcher's certificate. The certificate is generated on your
machine and never leaves it.

1. In the **Server** tab, click **Generate…** under **HTTPS certificate**.
2. Pick a folder and a name (default `neoproxy-cert`). NeoCatcher writes three files:

    | File | Used by |
    | --- | --- |
    | `.cer` | Devices, browsers and operating systems |
    | `.jks` | The proxy itself (keystore) |
    | `.p12` | Tools that expect PKCS#12 |

3. Keystore passwords are kept in the IDE's password safe, not in project files.

Already have a keystore? Use **Use Existing…** instead.

## 4. Start the proxy

In the **Server** tab, click **Start**. The proxy listens on `127.0.0.1:9942` unless you change it in the settings (gear icon). Devices on your Wi-Fi can connect only after you allow it there.

## 5. Connect your client

Click **Connect a Client…** in the Server tab and pick what you want to debug:

| Client | What the wizard does |
| --- | --- |
| Android emulator | Installs the certificate (as a system certificate on Google APIs images), sets the emulator proxy, adds a debug-only trust config to your app |
| Android phone | Tunnels the proxy over USB (`adb reverse`), copies the certificate and opens the right Settings screen |
| Java / Kotlin app | Adds proxy and truststore VM options to a run configuration, or imports the certificate into a JDK |
| Browser | Opens Chrome, Edge or Firefox in a separate profile that uses the proxy |
| This computer | Trusts the certificate in the operating system store |
| iPhone / iOS | Guides you through the proxy, profile and trust settings |
| Terminal & scripts | Gives you the environment variables for curl, Node, Python and Go |

Every flow ends with **Verify**: it waits for a decrypted HTTPS request from your client, so you know the setup
works. Prefer doing it by hand? See [Device setup](device-setup.md).

## 6. See your first request

Make a request from your app. It appears in **Request Log** within a second. Select it to see headers and body,
or right-click it to **Copy as cURL** or **Add Response Breakpoint…**.

Next: [write your first rule](rules.md), or [connect your AI agent](mcp.md) so it can read this traffic too.
