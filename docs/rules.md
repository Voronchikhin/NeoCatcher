# Rules

Rules change traffic automatically: redirect a host, add a header, mock a body, force an error status.

- **Request Mappings** change requests before they reach the server.
- **Response Mappings** change responses before they reach your app.

Each rule has a checkbox in the list (or press ++space++) to turn it on and off without deleting it.
Disabled rules stay in place, greyed out, and keep their order.

!!! info "Free and Pro"
    The free edition runs up to three active rules at a time. [Pro](pricing.md) removes the limit.

## Editing a rule

The editor has three modes that stay in sync:

- **Visual** — a form with conditions on one side and modifiers on the other.
- **YAML** and **JSON** — full source with completion, inline validation and quick documentation
  (uses the IDE's bundled JSON/YAML support).

![The Visual editor: URL conditions on the left, header, body and status modifiers on the right](assets/media/rule-editor-visual.webp){ loading=lazy }

![YAML mode with a completion popup offering the body actions replace and set](assets/media/feature-rules.webp){ loading=lazy }

Invalid drafts are kept, and errors point to the exact field (`conditions.any[0].all[1] ...`) or YAML line and column.
Click **Save Changes** to apply.

## How matching works

```yaml
conditions:
  any:          # OR: the rule matches when any block matches
    - all:      # AND: every condition in the block must match
        - ...
```

| Condition `type` | Checks |
| --- | --- |
| `url` | `target`: `host`, `path` or `wholeUrl` |
| `query` | A query parameter |
| `header` | A request or response header |
| `body` | A request or response body |
| `status` | The response status code (response rules) |
| `all` | Every response |

Operators: `equals` and `contains` compare literal text, `glob` matches the whole value (`*` any text, `?` one
character), `regex` searches the value. New conditions start with **Glob**: a plain value such as `api.example.com`
still matches exactly, and you add `*` when you need it (`*.example.com`, `/api/*`).

Modifiers run top to bottom, by category: **URL → Headers → Body → Query** for requests, **Headers → Body → Status
→ Delay** for responses.

## Examples

### Mock a server error

```yaml
name: Login returns 500
conditions:
  any:
    - all:
        - type: url
          target: path
          operator: equals
          value: /api/login
modifiers:
  status:
    - action: set
      value: "500"
  body:
    - action: set
      value: '{"error": "server_down"}'
```

### Send the app to staging

```yaml
name: Use staging API
conditions:
  any:
    - all:
        - type: url
          target: host
          operator: equals
          value: api.example.com
modifiers:
  url:
    - action: setHost
      value: staging.example.com
      updateHostHeader: true
```

### Serve a response from a file in your project

Like Charles' *Map Local*: keep mock JSON next to your code, edit it in the IDE, and the next request gets the new
version. In the Visual editor choose **Set from file** and pick the file; the path is stored relative to the project,
so the rule works wherever the project is checked out.

```yaml
name: Orders from a mock file
conditions:
  any:
    - all:
        - type: url
          target: path
          operator: glob
          value: /api/orders*
modifiers:
  body:
    - action: setFile
      value: mocks/orders.json
```

The response keeps its status and headers, including `Content-Type`. If the file can't be read, the response is
sent unchanged.

### Simulate a slow network

Hold matching responses to see loading states, spinners and timeouts:

```yaml
name: Slow search
conditions:
  any:
    - all:
        - type: url
          target: path
          operator: glob
          value: /api/search*
modifiers:
  delay:
    - action: set
      value: "3000"   # milliseconds, up to 60000
```

### Add a debug header to every response

```yaml
name: Debug header
conditions:
  any:
    - all:
        - type: all
modifiers:
  headers:
    - action: add
      name: X-Debug
      value: neocatcher
```

## Modifier reference

| Rules | Category | Actions |
| --- | --- | --- |
| Request | `url` | `setHost`, `setPath`, `setUrl`, `replaceHost`, `replacePath` |
| Both | `headers` | `add` (keep existing), `update` (replace all with this name), `remove` |
| Both | `body` | `set` (whole body), `replace` (every occurrence of literal text) |
| Response | `body` | `setFile` (the whole body from a file; relative paths start at the project directory) |
| Request | `query` | Change query parameters |
| Response | `status` | `set` (a code from 100 to 599, quoted) |
| Response | `delay` | `set` (milliseconds from 0 to 60000, quoted; several delays add up) |

The editor's completion lists every field with its documentation, so you rarely need this table.
