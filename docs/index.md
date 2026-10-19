---
title: NeoCatcher
hide:
  - navigation
  - toc
---

# NeoCatcher

**Catch, inspect and change your app's HTTP(S) traffic without leaving the IDE.**

NeoCatcher is a debugging proxy that lives in IntelliJ IDEA, Android Studio and other JetBrains IDEs.
Point your app or emulator at it and every request shows up in a tool window next to your code.

[Get started](getting-started.md){ .md-button .md-button--primary }

<div class="showcase" markdown>

<div markdown>

### 1. Easy setup

The Connect wizard installs the certificate, routes the traffic and confirms your first decrypted request, for
Android emulators, phones, JVM apps and browsers. No `adb` commands to type.

[Getting started](getting-started.md){ .md-button }

</div>

<video autoplay loop muted playsinline controls poster="assets/media/easy-setup.webp" width="1680" height="1050"
       aria-label="The Connect a Client wizard sets up an Android emulator in four steps, then the app's HTTPS request appears decrypted in the Request Log">
  <source src="assets/media/easy-setup.mp4" type="video/mp4">
</video>

</div>

<div class="showcase showcase--reverse" markdown>

<div markdown>

### 2. Works with your AI agent

Claude Code, Cursor, VS Code and any MCP client can read the captured traffic, explain a failing call and, if you
allow it, mock a response for you. It runs locally and is protected by a token.

[Set up MCP](mcp.md){ .md-button }

</div>

```bash
claude mcp add --transport http neocatcher \
  http://127.0.0.1:9950/mcp \
  --header "Authorization: Bearer <token>"
```

</div>

<div class="showcase" markdown>

<div markdown>

### 3. Live breakpoints

Pause a response while your app waits, change its status, headers or body, then send it on, and see the diff of
what changed. Or abort the call to test your error handling.

[Breakpoints](breakpoints.md){ .md-button }

</div>

<video autoplay loop muted playsinline controls poster="assets/media/home-hero.webp" width="1680" height="1050"
       aria-label="A response from an Android app is paused in NeoCatcher, changed to an error and the app shows the error card">
  <source src="assets/media/home-hero.mp4" type="video/mp4">
</video>

</div>

<div class="showcase showcase--reverse" markdown>

<div markdown>

### 4. Rules you write in seconds

Mock a body, add a header or force a status code. Write the rule in a form, or in YAML and JSON with completion,
documentation and inline errors.

[Rules](rules.md){ .md-button }

</div>

<div markdown>

=== "Visual"

    ![The Visual rule editor: URL conditions on the left, body and status modifiers on the right](assets/media/rule-editor-visual.webp){ loading=lazy }

=== "YAML"

    ![YAML rule editor with a completion popup offering replace and set](assets/media/feature-rules.webp){ loading=lazy }

</div>

</div>

## And more

<div class="grid cards" markdown>

-   **Request log in your IDE**

    ---

    Every request and response, with headers, formatted bodies and a diff of what your rules changed.
    Copy any request as cURL.

-   **Rules that mock and rewrite**

    ---

    Redirect hosts, change headers, replace bodies, force a status code. Write rules in a form,
    YAML or JSON with completion and validation.

-   **Response breakpoints**

    ---

    Pause a live response, edit its status, headers or body, then send it on — or abort the call
    to test your error handling.

-   **Built for Android developers**

    ---

    The Connect wizard installs the certificate and routes traffic for emulators, phones, JVM apps and browsers — then verifies it works.

-   **Works with your AI agent**

    ---

    Claude Code, Cursor, VS Code and other MCP clients can read captured traffic and, with your permission,
    mock responses for you. [Set it up](mcp.md).

</div>

## How it works

1. NeoCatcher starts a local HTTP(S) proxy on your machine (port `9942` by default).
2. Your app, emulator, browser or JVM process sends its traffic through that proxy.
3. NeoCatcher decrypts HTTPS with a CA certificate that only exists on your machine,
   applies your rules and breakpoints, and shows everything in the tool window.

Nothing leaves your computer: NeoCatcher does not send your traffic, or data about it, anywhere.
See [Security](security.md) and [Privacy](privacy.md).

## Free and Pro

The request log, certificate setup and up to three active rules are free forever.
Pro adds unlimited rules, rules shared through git, and breakpoints. [See pricing](pricing.md).
