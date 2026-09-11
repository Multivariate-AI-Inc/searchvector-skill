# SearchVector Skill

Authoritative Codex skill for working with the [SearchVector API](https://searchvector.io).

SearchVector is an SEO platform with APIs for projects, Google Search Console insights, Google indexing, rank tracking, keyword research, Google Ads, GA4, Google Business Profile, YouTube, Apple Search Ads, CMS integrations, AI content tools, automations, and billing.

## What this skill does

Use this skill whenever you need to:

- Find the correct SearchVector API endpoint, method, parameters, or request body
- Write or review code that calls `searchvector.io`
- Debug SearchVector API requests
- Understand authentication, pagination, response schemas, or error behavior

The generated reference files are the source of truth. The skill checks the endpoint index first, then reads the matching API reference before suggesting or writing a request. This helps avoid guessed paths, fields, and enum values.

## Making API requests

For server-side integrations, set an API token in the environment:

```bash
export SEARCHVECTOR_API_TOKEN="your-token"
```

Then use the bundled client. It adds the required authentication, JSON headers, and browser-like `User-Agent` automatically:

```bash
python scripts/sv_request.py GET /api/projects/
python scripts/sv_request.py GET /api/projects/ -q search=nike -q page=2
python scripts/sv_request.py POST /api/projects/ \
  -d '{"name":"My Site","website_url":"https://example.com"}'
```

JWT authentication is also supported through `SEARCHVECTOR_JWT`:

```bash
export SEARCHVECTOR_JWT="your-jwt"
```

Never hardcode or paste credentials into source code, command history, or chat. Keep the trailing slash in API paths; Django treats `/api/projects/` and `/api/projects` differently.

## Reference files

`references/_index.md` is the endpoint index. The topic files contain the detailed endpoint and response-schema documentation:

- `auth.md` — authentication and user/profile endpoints
- `projects.md` — projects, members, roles, invitations, and integrations
- `gsc-indexing.md` — Search Console insights and Google indexing
- `seo-tools.md` — keyword research, rank tracking, SERP, and performance
- `seo-tasks.md` — SEO tasks and comments
- `content.md` and `ai-tools.md` — content and AI tools
- `google-ads.md`, `analytics.md`, `gmb.md`, `youtube.md`, and `apple-ads.md` — platform integrations
- `cms.md` — Webflow and WordPress CMS
- `automations.md` and `billing.md` — automations, credits, and billing
- `misc.md` — notifications, changelog, contact, and other APIs

## Updating the references

The references are generated from the SearchVector OpenAPI specification. Regenerate them with:

```bash
python scripts/gen_refs.py path/to/openapi.yaml references/
```

Interactive API documentation is available at [searchvector.io/api/redoc/](https://searchvector.io/api/redoc/).
