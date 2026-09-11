# SearchVector Skill

AI-agent skill for working with the [SearchVector API](https://searchvector.io).

Use it to find endpoints, inspect request/response schemas, write integrations, debug API calls, and refresh API reference docs from the production OpenAPI schema used by [Redoc](https://searchvector.io/api/redoc/).

## Requirements

- Python 3, available as `python` or `python3`
- Optional: `PyYAML` for YAML schema parsing
- SearchVector account for authenticated API calls
- API token from [SearchVector API Token](https://searchvector.io/dashboard/api-token) when calling protected endpoints

Docs lookup and live schema search do not require a token. Real API calls require `SEARCHVECTOR_API_TOKEN` or `SEARCHVECTOR_JWT`.
If your system uses `python3`, replace `python` with `python3` in the examples below.

## Install For An Agent

Clone this repo and make the folder available to your AI agent as a skill.

```bash
git clone https://github.com/Multivariate-AI-Inc/searchvector-skill.git
```

For Codex, place or link the folder in your Codex skills directory, then invoke:

```text
Use $searchvector-api to find the right SearchVector API endpoint.
```

For other agents, instruct them to read `SKILL.md` first, then use `references/_index.md` and `scripts/sv_api.py`.

## Quick Start

Search live API schema:

```bash
python scripts/sv_api.py search "rank tracker keyword" --refresh
python scripts/sv_api.py show rank_tracker_keywords_list
```

Call an API:

```bash
export SEARCHVECTOR_API_TOKEN="your-token"
python scripts/sv_api.py call GET /api/projects/
python scripts/sv_api.py call GET /api/projects/ --query search=nike
```

Never paste tokens into chat, source code, or command examples shared publicly.

## How Agents Should Use This

1. Search `references/_index.md` first.
2. Open only the matching topic file in `references/`.
3. Use `scripts/sv_api.py search/show` when current schema details matter.
4. Use `scripts/sv_api.py call` only when the user has configured auth and approved the API call.

## Reference Files

`references/_index.md` is the endpoint index. Topic files cover auth, projects, GSC/indexing, SEO tools, SEO tasks, content, AI tools, Google Ads, analytics, Google Business Profile, YouTube, Apple Search Ads, CMS, automations, billing, and misc APIs.

## Update API Docs

Docs do not update automatically. Refresh them manually:

```bash
python scripts/sv_api.py update-docs --dry-run
python scripts/sv_api.py update-docs
python scripts/sv_api.py validate
```

Deprecated endpoints are skipped when the OpenAPI schema marks them deprecated. Account or plan restrictions may still require handling `401`, `403`, or documented API errors.

## Release

After the first public push, tag a stable release such as `v1.0.0`.
