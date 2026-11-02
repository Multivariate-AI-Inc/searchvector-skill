# SearchVector Skill

AI-agent skill for working with the [SearchVector API](https://searchvector.io).

Use it to find endpoints, inspect request/response schemas, write integrations, debug API calls, and refresh API reference docs from the production OpenAPI schema used by [Redoc](https://searchvector.io/api/redoc/).

## Requirements

- Python 3, available as `python` or `python3`
- Optional: `PyYAML` for YAML schema parsing
- SearchVector account for authenticated API calls
- API token from [SearchVector API Token](https://searchvector.io/dashboard/api-token) when calling protected endpoints

Docs lookup and live schema search do not require a token. Real API calls require a saved token from setup, `SEARCHVECTOR_API_TOKEN`, or `SEARCHVECTOR_JWT`.
If your system uses `python3`, replace `python` with `python3` in the examples below.

## Install For An Agent

Install with the [Skills CLI](https://github.com/vercel-labs/skills) (requires Node.js and npm):

```bash
npx skills add Multivariate-AI-Inc/searchvector-skill
```

Follow the prompts to choose your coding agent and installation scope.

To install specifically for Codex or Claude Code:

```bash
npx skills add Multivariate-AI-Inc/searchvector-skill --agent codex
npx skills add Multivariate-AI-Inc/searchvector-skill --agent claude-code
```

Add `--global` to make the skill available across projects. To preview the available skill without installing it:

```bash
npx skills add Multivariate-AI-Inc/searchvector-skill --list
```

### Manual Installation

Alternatively, clone this repo and make the folder available to your AI agent as a skill.

```bash
git clone https://github.com/Multivariate-AI-Inc/searchvector-skill.git
```

For Codex, place or link the folder in your Codex skills directory, then invoke:

```text
Use $searchvector-api to find the right SearchVector API endpoint.
```

For other agents, instruct them to read `SKILL.md` first, then use `references/_index.md` and `scripts/sv_api.py`.

## Set Up Your API Token

Your coding agent checks for credentials before its first authenticated task. If they are missing, it launches setup for you in a separate terminal. Sign in to SearchVector, copy your token, and paste it into that terminal's hidden prompt. The agent checks configuration again after you finish and continues your task.

The agent uses these commands from the installed skill folder:

```bash
python scripts/sv_api.py auth-status
python scripts/sv_api.py setup --launch
```

Automatic terminal launching supports macOS Terminal and common desktop Linux terminals (`x-terminal-emulator`, GNOME Terminal, Konsole, or xterm). It runs on the same machine as the agent. In headless/remote environments, unsupported platforms, or when terminal launching is blocked, setup reports a manual fallback.

You can also start setup yourself from the installed skill folder (or cloned repository):

```bash
python scripts/sv_api.py setup
```

This opens the SearchVector token page in your default browser. Sign in, copy your token, and paste it into the hidden terminal prompt. The helper saves it locally and loads it automatically for future API calls—no shell configuration changes or agent restart required.

The token is stored as unencrypted JSON at `~/.config/searchvector/credentials.json` (or `$XDG_CONFIG_HOME/searchvector/credentials.json` if configured), with owner-only file permissions (`600`) and directory permissions (`700`). Keep this file private. Run setup again to replace the saved token, or delete the file to remove it locally. Removing the file does not revoke the token in SearchVector.

If the browser cannot open, use the link printed by setup. You can also run `python scripts/sv_api.py setup --no-browser`. Setup requires an interactive terminal; paste your token there, never in agent chat.

### Optional: Configure Through Your Shell

Environment credentials take precedence over the saved token: `SEARCHVECTOR_API_TOKEN`, then `SEARCHVECTOR_JWT`, then the saved token. Use the following only if you prefer environment variables or need them for your own integration code.

1. Sign in to SearchVector and open [SearchVector API Token](https://searchvector.io/dashboard/api-token).
2. Copy your API token from that page. Keep it private; enter it locally in your shell configuration, not in the agent chat.
3. Open the configuration file for your shell in a text editor:

   | Shell | Open configuration | Reload after saving |
   | --- | --- | --- |
   | Zsh (default on modern macOS) | `nano ~/.zshrc` | `source ~/.zshrc` |
   | Bash | `nano ~/.bashrc` | `source ~/.bashrc` |

   If you're unsure which shell you use, run `echo "$SHELL"`. Bash login shells may read `~/.bash_profile` instead; ensure it sources `~/.bashrc`, or put the export in the startup file your terminal reads.

4. Add this line, replacing the placeholder with your token, then save the file:

   ```bash
   export SEARCHVECTOR_API_TOKEN='your-token'
   ```

   Editing the file directly keeps the token out of shell command history.

5. Run the matching reload command from the table, then check that the variable is set without printing its value:

   ```bash
   if [ -n "${SEARCHVECTOR_API_TOKEN:-}" ]; then
     printf 'SearchVector API token is configured.\n'
   else
     printf 'SearchVector API token is missing.\n'
   fi
   ```

6. Start your coding agent from that terminal so it inherits the variable. Restart an already-running agent after configuring the token. A desktop app launched from the Dock or application launcher may not inherit your terminal environment; use the app's supported environment configuration or launch it from the configured terminal.

The helper reads saved credentials and environment variables; it does not automatically load `.env` files. Never commit your token or paste it into chat. Docs lookup does not require a token.

## Quick Start

Run these examples from the installed skill folder (or the cloned repository), where `scripts/` is available.

Search live API schema:

```bash
python scripts/sv_api.py search "rank tracker keyword" --refresh
python scripts/sv_api.py show rank_tracker_keywords_list
```

After completing the token setup above, call an API:

```bash
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
