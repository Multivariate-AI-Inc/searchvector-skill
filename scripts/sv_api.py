#!/usr/bin/env python3
"""Search, inspect, call, and refresh SearchVector OpenAPI references."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://searchvector.io"
DEFAULT_SCHEMA_URL = DEFAULT_BASE_URL + "/api/schema/"
CACHE_PATH = Path(os.environ.get("SEARCHVECTOR_SCHEMA_CACHE", "/tmp/searchvector-openapi.yaml"))
DEFAULT_USER_AGENT = "Mozilla/5.0 (compatible; searchvector-skill/1.0)"
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
PUBLIC_EXCLUDE_RE = re.compile(r"\b" + "in" + "ternal" + r"\b", re.I)
PUBLIC_SECURITY_SCHEMES = {"BearerAuth", "tokenAuth", "cookieAuth"}


def die(message: str, code: int = 1) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(code)


def fetch_url(url: str, headers: dict[str, str] | None = None, data: bytes | None = None, method: str | None = None) -> bytes:
    request = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        die(f"HTTP {exc.code} for {url}\n{body[:4000]}")
    except urllib.error.URLError as exc:
        die(f"request failed for {url}: {exc.reason}")


def load_schema_text(schema_url: str, refresh: bool) -> str:
    if CACHE_PATH.exists() and not refresh:
        return CACHE_PATH.read_text(encoding="utf-8")
    raw = fetch_url(schema_url, headers={"Accept": "application/yaml, application/json", "User-Agent": DEFAULT_USER_AGENT})
    text = raw.decode("utf-8", "replace")
    CACHE_PATH.write_text(text, encoding="utf-8")
    return text


def load_schema(schema_url: str, refresh: bool) -> dict[str, Any]:
    text = load_schema_text(schema_url, refresh)
    stripped = text.lstrip()
    if stripped.startswith("{"):
        loaded = json.loads(text)
    elif yaml is not None:
        loaded = yaml.safe_load(text)
    else:
        die("PyYAML is required to parse YAML schemas. Install pyyaml or use a JSON schema URL.")
    if not isinstance(loaded, dict):
        die("schema did not parse to an object")
    return loaded


def has_private_text(value: Any) -> bool:
    if isinstance(value, dict):
        return any(has_private_text(v) for v in value.values())
    if isinstance(value, list):
        return any(has_private_text(v) for v in value)
    return isinstance(value, str) and PUBLIC_EXCLUDE_RE.search(value) is not None


def is_public_operation(operation: dict[str, Any]) -> bool:
    if operation.get("deprecated"):
        return False
    return not has_private_text(
        {
            "tags": operation.get("tags", []),
            "summary": operation.get("summary", ""),
            "description": operation.get("description", ""),
            "operationId": operation.get("operationId", ""),
        }
    )


def public_security(security: Any) -> Any:
    if not isinstance(security, list):
        return security
    cleaned = []
    for item in security:
        if not isinstance(item, dict):
            continue
        public_item = {key: value for key, value in item.items() if key in PUBLIC_SECURITY_SCHEMES}
        if public_item or not item:
            cleaned.append(public_item)
    return cleaned


def iter_operations(schema: dict[str, Any]) -> list[dict[str, Any]]:
    ops: list[dict[str, Any]] = []
    for path, path_item in (schema.get("paths") or {}).items():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            if not is_public_operation(operation):
                continue
            haystack = "\n".join(
                str(x)
                for x in [
                    path,
                    method.upper(),
                    operation.get("operationId", ""),
                    operation.get("summary", ""),
                    operation.get("description", ""),
                    " ".join(operation.get("tags") or []),
                ]
            )
            ops.append({"path": path, "method": method.upper(), "operation": operation, "haystack": haystack})
    return ops


def score_operation(op: dict[str, Any], terms: list[str]) -> int:
    text = op["haystack"].lower()
    score = 0
    for term in terms:
        if term in text:
            score += 10
        for token in term.split():
            if token and token in text:
                score += 2
    return score


def cmd_search(args: argparse.Namespace) -> None:
    schema = load_schema(args.schema_url, args.refresh)
    terms = [args.query.lower()]
    terms.extend(t.lower() for t in re.split(r"[\s/_-]+", args.query) if t)
    matches = []
    for op in iter_operations(schema):
        score = score_operation(op, terms)
        if score:
            matches.append((score, op))
    matches.sort(key=lambda item: (-item[0], item[1]["path"], item[1]["method"]))
    for score, op in matches[: args.limit]:
        operation = op["operation"]
        print(f"{op['method']:6} {op['path']}")
        print(f"  operationId: {operation.get('operationId', '')}")
        if operation.get("tags"):
            print(f"  tags: {', '.join(operation.get('tags') or [])}")
        if operation.get("summary"):
            print(f"  summary: {operation.get('summary')}")
        print(f"  score: {score}")


def find_operation(schema: dict[str, Any], selector: str, method: str | None = None) -> dict[str, Any]:
    selector_l = selector.lower()
    for op in iter_operations(schema):
        operation = op["operation"]
        if method and op["method"].lower() != method.lower():
            continue
        if selector == op["path"] or selector_l == str(operation.get("operationId", "")).lower():
            return op
    for op in iter_operations(schema):
        if method and op["method"].lower() != method.lower():
            continue
        if selector_l in op["haystack"].lower():
            return op
    die(f"operation not found: {selector}")


def cmd_show(args: argparse.Namespace) -> None:
    schema = load_schema(args.schema_url, args.refresh)
    op = find_operation(schema, args.selector, args.method)
    operation = op["operation"]
    print(f"{op['method']} {op['path']}")
    for key in ["operationId", "summary", "description", "tags", "parameters", "requestBody", "responses", "security"]:
        if key in operation:
            value = public_security(operation[key]) if key == "security" else operation[key]
            print(f"\n{key}:")
            print(textwrap.indent(json.dumps(value, indent=2, ensure_ascii=False), "  "))


def auth_headers() -> dict[str, str]:
    token = os.environ.get("SEARCHVECTOR_API_TOKEN")
    jwt = os.environ.get("SEARCHVECTOR_JWT")
    if not token and not jwt:
        die("missing SEARCHVECTOR_API_TOKEN or SEARCHVECTOR_JWT. Configure auth in the environment before calling APIs.")
    return {"Authorization": f"Token {token}" if token else f"Bearer {jwt}"}


def cmd_call(args: argparse.Namespace) -> None:
    base = os.environ.get("SEARCHVECTOR_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    if not args.path.startswith("/"):
        die("path must start with /api/...")
    url = base + args.path
    query_params = [tuple(q.split("=", 1)) if "=" in q else (q, "") for q in args.query]
    query = urllib.parse.urlencode(query_params)
    if query:
        url += ("&" if "?" in url else "?") + query

    headers = {"Accept": "application/json", "User-Agent": DEFAULT_USER_AGENT}
    headers.update(auth_headers())
    for header in args.header:
        if ":" not in header:
            die(f"invalid header, expected 'Name: value': {header}")
        name, value = header.split(":", 1)
        headers[name.strip()] = value.strip()

    data = None
    if args.json_body is not None:
        data = json.dumps(json.loads(args.json_body)).encode("utf-8")
        headers["Content-Type"] = "application/json"

    body = fetch_url(url, headers=headers, data=data, method=args.method.upper()).decode("utf-8", "replace")
    try:
        print(json.dumps(json.loads(body), indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(body)


def count_index_entries(index_path: Path) -> int:
    if not index_path.exists():
        return 0
    return sum(1 for line in index_path.read_text(encoding="utf-8").splitlines() if re.match(r"^\w+ /api/", line))


def cmd_update_docs(args: argparse.Namespace) -> None:
    schema_text = load_schema_text(args.schema_url, refresh=True)
    schema_path = CACHE_PATH
    schema_path.write_text(schema_text, encoding="utf-8")
    gen_refs = ROOT / "scripts" / "gen_refs.py"
    references = ROOT / "references"
    before = count_index_entries(references / "_index.md")
    if args.dry_run:
        with tempfile.TemporaryDirectory() as tempdir:
            temp_refs = Path(tempdir) / "references"
            subprocess.run([sys.executable, str(gen_refs), str(schema_path), str(temp_refs)], check=True)
            after = count_index_entries(temp_refs / "_index.md")
        print(f"dry run: {before} current endpoints, {after} endpoints from {args.schema_url}")
        return
    subprocess.run([sys.executable, str(gen_refs), str(schema_path), str(references)], check=True)
    print(f"updated {references} from {args.schema_url}")
    print(f"endpoint count: {before} -> {count_index_entries(references / '_index.md')}")


def cmd_validate(args: argparse.Namespace) -> None:
    root = Path(args.root).resolve()
    required = [
        root / "SKILL.md",
        root / "README.md",
        root / "agents" / "openai.yaml",
        root / "references" / "_index.md",
        root / "scripts" / "sv_api.py",
        root / "scripts" / "gen_refs.py",
    ]
    errors = []
    for path in required:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(root)}")

    index_count = count_index_entries(root / "references" / "_index.md")
    if index_count == 0:
        errors.append("references/_index.md has no API entries")

    forbidden_terms = [
        "stag" + "ing",
        "sv-" + "stag" + "ing",
        "maa" + "keetoo",
        "SV_" + "TOKEN",
        "imperson" + "ation",
        r"\b" + "in" + "ternal" + r"\b",
    ]
    forbidden = re.compile("|".join(forbidden_terms), re.I)
    ignored_dirs = {".git", ".pycache", "__pycache__"}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in ignored_dirs for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if forbidden.search(line):
                errors.append(f"forbidden public term: {path.relative_to(root)}:{lineno}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"validation passed: {index_count} API entries, no forbidden public terms")


def cmd_legacy_request(args: argparse.Namespace) -> None:
    translated = argparse.Namespace(method=args.method, path=args.path, query=args.query, json_body=None, header=[])
    if args.data is not None:
        raw = sys.stdin.read() if args.data == "@-" else (Path(args.data[1:]).read_text(encoding="utf-8") if args.data.startswith("@") else args.data)
        json.loads(raw)
        translated.json_body = raw
    cmd_call(translated)


def add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--schema-url", default=argparse.SUPPRESS)
    parser.add_argument("--refresh", action="store_true", default=argparse.SUPPRESS)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search, inspect, call, and refresh SearchVector APIs.")
    parser.set_defaults(schema_url=os.environ.get("SEARCHVECTOR_SCHEMA_URL", DEFAULT_SCHEMA_URL), refresh=False)
    add_common_options(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="search OpenAPI operations")
    add_common_options(search)
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    search.set_defaults(func=cmd_search)

    show = sub.add_parser("show", help="show operation details by operationId, path, or text")
    add_common_options(show)
    show.add_argument("selector")
    show.add_argument("--method")
    show.set_defaults(func=cmd_show)

    call = sub.add_parser("call", help="call an API endpoint")
    add_common_options(call)
    call.add_argument("method", choices=["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"])
    call.add_argument("path")
    call.add_argument("--query", action="append", default=[])
    call.add_argument("--json", dest="json_body")
    call.add_argument("--header", action="append", default=[])
    call.set_defaults(func=cmd_call)

    update_docs = sub.add_parser("update-docs", help="refresh generated references from the OpenAPI schema used by Redoc")
    update_docs.add_argument("--schema-url", default=argparse.SUPPRESS)
    update_docs.add_argument("--dry-run", action="store_true", help="generate into a temporary directory without changing references")
    update_docs.set_defaults(func=cmd_update_docs)

    validate = sub.add_parser("validate", help="validate public skill files and generated references")
    validate.add_argument("--root", default=str(ROOT), help="skill root to validate")
    validate.set_defaults(func=cmd_validate)

    legacy = sub.add_parser("_legacy-request", help=argparse.SUPPRESS)
    legacy.add_argument("method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"])
    legacy.add_argument("path")
    legacy.add_argument("-q", "--query", action="append", default=[])
    legacy.add_argument("-d", "--data")
    legacy.set_defaults(func=cmd_legacy_request)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
