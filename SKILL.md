---
name: searchvector-api
description: Authoritative reference for the SearchVector API (searchvector.io) — an SEO platform covering projects, GSC insights, Google indexing, rank tracking, keyword research, Google Ads, GA4, Google My Business, YouTube, Apple Search Ads, Webflow/WordPress CMS, AI content tools, article generation, SEO tasks, automations, and billing. Use this skill whenever writing code that calls the SearchVector API, integrating with searchvector.io, debugging SearchVector requests, or answering any question about SearchVector endpoints, parameters, auth, or schemas — even if the user only mentions a feature area (e.g. "rank tracker API", "indexing endpoint") without naming SearchVector explicitly. Never answer SearchVector API questions from memory; always consult the reference files here.
---

# SearchVector API

Django REST Framework API. Base URL: `https://searchvector.io` (paths below already include `/api/`). Interactive docs: `https://searchvector.io/api/redoc/`.

## Accuracy rules (why this skill exists)

The reference files in `references/` are machine-generated from the service's OpenAPI spec. Use them first for token-efficient lookup, and use the live schema helper when freshness matters. LLM memory about this API is unreliable, so:

1. Never state or code against an endpoint, parameter, field, or enum value that you have not just read in `references/` or inspected with `scripts/sv_api.py show`.
2. Before writing any request, look up the exact endpoint (workflow below) and copy the path, method, params, and body fields verbatim.
3. Trailing slashes are significant (Django). Use paths exactly as written — `/api/projects/`, not `/api/projects`.
4. If asked about behavior the spec doesn't document (rate limits, exact error bodies), say it's not in the spec rather than inventing it.
5. Deprecated endpoints are excluded from generated references and live helper search/show results.

## Finding an endpoint (do this first, every time)

1. Grep the flat index: `grep -i "keyword" references/_index.md` (390 endpoints, one line each: `METHOD path → file — summary`).
2. Open only the reference file the index points to, and read only the matching `### METHOD /path` block plus the `## Response schemas` entries it mentions.
3. If the endpoint may be newer than the generated docs, search the live OpenAPI schema:

```bash
python scripts/sv_api.py search "rank tracker keyword" --refresh
python scripts/sv_api.py show rank_tracker_keywords_list
```

4. Don't load multiple reference files speculatively — each is 2–24 KB; load on demand only.

## Reference files

| File | Covers |
|---|---|
| references/auth.md | Google One Tap/OAuth login, JWT refresh/logout, per-service OAuth connections, user, profile |
| references/projects.md | Projects CRUD, members, roles, invitations, integrations |
| references/gsc-indexing.md | GSC insights, Google Indexing API, indexing activity logs |
| references/seo-tools.md | SEO tools, keyword research, rank tracker, SERP, performance |
| references/seo-tasks.md | SEO tasks and task comments |
| references/content.md | Article generator, content calendar |
| references/ai-tools.md | AI tools + experiments (SEO meta generation, apps, etc.) |
| references/google-ads.md | Google Ads |
| references/analytics.md | GA4, analytics, dashboard APIs |
| references/gmb.md | Google My Business |
| references/youtube.md | YouTube |
| references/apple-ads.md | Apple Search Ads |
| references/cms.md | Webflow CMS, WordPress |
| references/automations.md | Automation rules |
| references/billing.md | Billing, credits |
| references/misc.md | Notifications, changelog, contact, and other APIs |

## Authentication

Three schemes (an endpoint's `Auth:` line shows which it accepts):

- **JWT (primary)** — `Authorization: Bearer <access_token>`. Obtain the token from `POST /api/auth/google/one-tap/` or the OAuth flow (`GET /api/auth/google/authorize/` → `GET /api/auth/google/callback/`); refresh via the auth endpoints in `references/auth.md`.
- **Token (scripts/extensions)** — `Authorization: Token <api-key>` (DRF token auth). Availability depends on the account and product configuration.
- **Cookie** — Django `sessionid` cookie; used by the web app, not for integrations.

For server-side integrations and scripts, use Token auth; for user-facing flows, JWT.

**Making requests — use the bundled client, not raw curl**: `scripts/sv_api.py call` reads `SEARCHVECTOR_API_TOKEN` (or `SEARCHVECTOR_JWT`) from the environment, attaches the right Authorization header, and never prints the credential — so it can't leak into shell history or transcripts:

```bash
python scripts/sv_api.py call GET /api/projects/ --query search=nike
python scripts/sv_api.py call POST /api/projects/ --json '{"name":"My Site","website_url":"https://example.com"}'
```

If it reports the env var is unset, tell the user to `export SEARCHVECTOR_API_TOKEN=...` (in `~/.zshrc` or a gitignored `.env`) — never ask them to paste the key into chat, hardcode it, or pass it on a command line. When writing integration code for the user, read the token from that same env variable.

## Conventions

- **Pagination**: list endpoints return `{count, next, previous, results}`. Query params `page` and, where listed, `page_size` (max 100). `next`/`previous` are full URLs — follow them rather than computing offsets.
- **User-Agent required**: the server rejects requests without a browser-like `User-Agent` header. `scripts/sv_api.py` sends one automatically; any integration code you write must set one too (e.g. `Mozilla/5.0 (compatible; searchvector-client/1.0)`) — plain `curl` or default python-requests/urllib UAs will fail.
- **Bodies**: send JSON (`Content-Type: application/json`). Fields marked `*` in the references are required; `?` on a type means nullable; `[read-only]` fields are returned but must not be sent.
- **Responses**: `Returns:` lines list status codes and schema names; look up field lists under `## Response schemas` in the same file. `Paginated<X>` means the standard pagination wrapper around `X` items.
- **Errors**: standard DRF behavior — 400 with per-field error messages, 401 unauthenticated, 403 forbidden, 404 not found.

## Example lookup

Task: "create a project via the API"

```
grep -i "project" references/_index.md
# → POST /api/projects/ → projects.md — Create a new project
```

Then from `references/projects.md`:

```
POST https://searchvector.io/api/projects/
Authorization: Bearer <jwt>
{"name": "My Site", "website_url": "https://example.com"}   # name*, website_url* required
# → 201 ProjectCreate
```

## Keeping this skill current

When the API changes, regenerate the references (never hand-edit them):

```
python scripts/gen_refs.py path/to/openapi.yaml references/
```

The Redoc UI at `https://searchvector.io/api/redoc/` is backed by the OpenAPI schema. To refresh the local schema cache and regenerate `references/_index.md` plus topic docs from that source, run:

```
python scripts/sv_api.py update-docs
```

This does not run automatically. Run it only when the user asks to update API docs, when you need current endpoint details, or before publishing refreshed skill docs. Preview endpoint-count changes without rewriting docs:

```
python scripts/sv_api.py update-docs --dry-run
```

Validate public-safety checks before publishing:

```
python scripts/sv_api.py validate
```

If an API is not available for the user's account or plan, the schema may still list it. Confirm by checking the endpoint's auth requirements and, if the user authorizes an API call, handling `401`, `403`, or documented error responses.
