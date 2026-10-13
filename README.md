# NeoCatcher website

Documentation and website for **NeoCatcher**, the HTTP(S) debugging proxy for JetBrains IDEs and Android Studio.

**Live site:** https://neocatcher.com/

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages by
[.github/workflows/pages.yml](.github/workflows/pages.yml) on every push to `main`. Pull requests are built with
`--strict`, so broken links fail the check.

## Edit locally

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt   # Windows; on macOS/Linux: .venv/bin/pip
.venv/Scripts/mkdocs serve                      # http://127.0.0.1:8000, reloads on save
```

Pages live in [docs/](docs); the menu is `nav` in [mkdocs.yml](mkdocs.yml).

## Layout

| Path | Content |
| --- | --- |
| `docs/index.md` | Home page |
| `docs/getting-started.md`, `device-setup.md` | Install, certificate, connecting clients |
| `docs/rules.md`, `breakpoints.md`, `request-log.md` | Features |
| `docs/mcp.md` | AI agents (MCP) |
| `docs/pricing.md`, `changelog.md` | Free vs Pro, releases |
| `docs/terms.md`, `privacy.md` | Legal — **drafts** until reviewed by a lawyer |
| `docs/downloads/neocatcher_mcp_bridge.py` | MCP stdio bridge offered on the MCP page; the source of truth is `scripts/` in the plugin repository — copy it here when it changes |

## Custom domain

`neocatcher.com` (registered at Hostinger) points to GitHub Pages:

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153 |
| CNAME | www | voronchikhin.github.io |

The domain is set in **Settings → Pages → Custom domain** with **Enforce HTTPS**, and verified for the account
(**GitHub → Settings → Pages → Add a domain**) so nobody else can use it with GitHub Pages.

## Feedback

Found a mistake in the docs? Use **Edit this page** on any page, or open an issue.
