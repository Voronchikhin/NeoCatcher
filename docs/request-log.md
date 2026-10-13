# Request log

The **Request Log** tab lists every exchange that passed through the proxy, newest first.

## Reading an exchange

Select an entry to open its preview. Switch between **Request** and **Response**, then between:

| View | Shows |
| --- | --- |
| Headers | All headers as sent and received |
| Body | The body, formatted for JSON, XML and other common types |
| Diff | What your rules and breakpoints changed: URL, headers and body for requests; status, headers and body for responses |

Entries changed by a rule or breakpoint are labelled with its name, so you can always tell what was real and what
was mocked.

## Filtering

Type in **Filter by URI...** above the list to keep only matching requests.

## Actions

Right-click an entry:

- **Copy as cURL** — a bash/zsh command that replays the request as the server received it.
- **Add Response Breakpoint…** — pause the next responses from this endpoint. See [Breakpoints](breakpoints.md).

## Clearing the log

Use the trash button: **Delete All Log Entries** or **Delete Old Log Entries**.

The log lives in the IDE's memory for the current session. It is not uploaded anywhere.
