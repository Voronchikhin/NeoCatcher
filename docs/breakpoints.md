# Breakpoints

A response breakpoint pauses matching responses so you can edit them before your app receives them —
like a debugger breakpoint, but for network calls.

!!! info "Pro feature"
    Breakpoints are part of [NeoCatcher Pro](pricing.md). The 30-day trial includes them. In Free you can see the
    Breakpoints tab, but responses do not pause.

## Add a breakpoint

- In **Request Log**, right-click a request → **Add Response Breakpoint…**, or
- In the **Breakpoints** tab, add a rule with a URL pattern (**Contains**, **Glob** or **Regex**) and an optional
  HTTP method, or
- Import one from an existing request or response rule (the conditions are copied; later rule changes don't
  affect the breakpoint).

A global switch turns all breakpoints off at once.

## When a response is paused

The **Breakpoints** tab title shows how many responses are waiting, for example **Breakpoints (2)**.
Select one to open the editor, change the **status**, **headers** or **body**, then:

| Action | Result |
| --- | --- |
| **Send** | Your app receives the response, with your edits |
| **Abort** | The call fails with a network error (NeoCatcher sends a `502` and closes the connection) |

The Request Log marks the exchange with a `Breakpoint · …` label and shows your edits in **Diff**.

## What a breakpoint sees

Breakpoints match the call as the server saw and answered it: the forwarded request and the upstream
status, headers and body — *before* response rules change them. A rule that hides a `500` still lets a breakpoint
catch that `500`. The editor shows the response exactly as it will be sent, after your rules.

## Limits

- Up to **20** responses can be paused at once; extra matches pass through with a warning.
- A paused response continues unchanged after **10 minutes**.
- Stopping the proxy or closing the project releases every paused response.
- Breakpoints pause **responses**. Request breakpoints are planned.
