#!/usr/bin/env python3
"""Generate token-efficient skill reference docs from openapi.yaml.
Every line of output is derived from the spec — no hand-written endpoint docs."""
import yaml, re, os, sys, collections

SPEC = sys.argv[1]
OUT = sys.argv[2]

spec = yaml.safe_load(open(SPEC))
schemas = spec.get("components", {}).get("schemas", {})

# tag -> reference file grouping
GROUPS = {
    "auth": ["Authentication", "auth", "Service OAuth", "User", "Profile", "UAC"],
    "projects": ["Projects", "Project Members", "Project Integrations", "Invitations"],
    "gsc-indexing": ["GSC Insights", "Google Indexing API", "Activity Logs"],
    "google-ads": ["Google Ads"],
    "analytics": ["Google Analytics 4", "Analytics", "Dashboard APIs"],
    "gmb": ["Google My Business"],
    "youtube": ["YouTube"],
    "apple-ads": ["Apple Search Ads"],
    "content": ["Article Generator", "Content Calendar"],
    "ai-tools": ["AI Tools", "AI Tools - Experiments"],
    "seo-tasks": ["SEO Tasks", "SEO Task Comments"],
    "seo-tools": ["SEO Tools", "Keyword Research", "Rank Tracker", "SERP Tools", "Performance Tools"],
    "cms": ["Webflow CMS", "WordPress"],
    "automations": ["Automations"],
    "billing": ["billing", "Credits"],
    "misc": ["Notifications", "Changelog", "What's New", "Contact", "Public API"],
}
tag2file = {t: f for f, ts in GROUPS.items() for t in ts}
PUBLIC_EXCLUDE_RE = re.compile(r"\b" + "in" + "ternal" + r"\b", re.I)

def has_private_text(value):
    if isinstance(value, dict):
        return any(has_private_text(v) for v in value.values())
    if isinstance(value, list):
        return any(has_private_text(v) for v in value)
    return isinstance(value, str) and PUBLIC_EXCLUDE_RE.search(value)

def is_public_operation(op):
    if op.get("deprecated"):
        return False
    return not has_private_text({
        "tags": op.get("tags", []),
        "summary": op.get("summary", ""),
        "description": op.get("description", ""),
        "operationId": op.get("operationId", ""),
    })

def deref(s):
    if isinstance(s, dict) and "$ref" in s:
        name = s["$ref"].split("/")[-1]
        return name, schemas.get(name, {})
    return None, s

def typestr(s):
    """Compact type string for a schema node."""
    name, s = deref(s)
    if name and not s:
        return name
    if not isinstance(s, dict):
        return "any"
    if "enum" in s:
        vals = s["enum"]
        shown = "|".join(str(v) for v in vals[:6])
        if len(vals) > 6:
            shown += f"|…{len(vals)-6} more"
        return f"enum({shown})"
    t = s.get("type")
    if t == "array":
        return f"array<{typestr(s.get('items', {}))}>"
    if t == "object" or (t is None and "properties" in s):
        return name or "object"
    if t is None and ("oneOf" in s or "anyOf" in s):
        alts = s.get("oneOf") or s.get("anyOf")
        return " | ".join(typestr(a) for a in alts[:4])
    out = t or "any"
    if s.get("format"):
        out += f"({s['format']})"
    if s.get("nullable"):
        out += "?"
    return out

def clean(txt, limit=180):
    if not txt:
        return ""
    txt = re.sub(r"\s+", " ", str(txt)).strip()
    return (txt[: limit - 1] + "…") if len(txt) > limit else txt

def is_paginated(s):
    p = s.get("properties", {})
    return {"count", "next", "previous", "results"} <= set(p)

def schema_fields(s, indent=0):
    """One line per property: name* (type) — desc"""
    lines = []
    _, s = deref(s)
    req = set(s.get("required", []))
    for prop, ps in s.get("properties", {}).items():
        if PUBLIC_EXCLUDE_RE.search(prop) or has_private_text(ps):
            continue
        star = "*" if prop in req else ""
        d = clean(ps.get("description", "") if isinstance(ps, dict) else "", 120)
        ro = " [read-only]" if isinstance(ps, dict) and ps.get("readOnly") else ""
        line = f"{'  '*indent}- {prop}{star} ({typestr(ps)}){ro}"
        if d:
            line += f" — {d}"
        lines.append(line)
    return lines

def resp_str(op, used):
    parts = []
    for code, r in sorted(op.get("responses", {}).items()):
        schema = r.get("content", {}).get("application/json", {}).get("schema")
        if schema is None:
            parts.append(f"{code}")
            continue
        name, resolved = deref(schema)
        if name and is_paginated(resolved):
            item = resolved["properties"]["results"].get("items", {})
            iname, _ = deref(item)
            extra = set(resolved["properties"]) - {"count", "next", "previous", "results"}
            extra_s = f" +{','.join(sorted(extra))}" if extra else ""
            if iname:
                used.add(iname)
            parts.append(f"{code} Paginated<{iname or typestr(item)}>{extra_s}")
        elif name:
            used.add(name)
            parts.append(f"{code} {name}")
        else:
            parts.append(f"{code} {typestr(schema)}")
    return " | ".join(parts)

def auth_str(op):
    secs = op.get("security", spec.get("security") or [])
    kinds = []
    for s in secs:
        for k in s:
            if k == "BearerAuth" and "JWT" not in kinds:
                kinds.append("JWT")
            elif k == "tokenAuth" and "Token" not in kinds:
                kinds.append("Token")
            elif k == "cookieAuth" and "Cookie" not in kinds:
                kinds.append("Cookie")
        if not s:
            kinds.append("none")
    return "/".join(kinds) or "JWT"

files = collections.defaultdict(list)   # file -> list of (path, method, op)
index_rows = []

for path, item in spec["paths"].items():
    for method in ("get", "post", "put", "patch", "delete"):
        if method not in item:
            continue
        op = item[method]
        if not is_public_operation(op):
            continue
        tag = (op.get("tags") or ["misc"])[0]
        f = tag2file.get(tag, "misc")
        files[f].append((path, method.upper(), op, item.get("parameters", [])))
        index_rows.append((path, method.upper(), f, clean(op.get("summary", ""), 60)))

os.makedirs(OUT, exist_ok=True)
total_ops = 0

for fname, ops in files.items():
    used_schemas = set()
    lines = [f"# SearchVector API — {fname}", ""]
    lines.append(f"Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. {len(ops)} endpoints.")
    lines.append("")
    for path, method, op, shared_params in sorted(ops):
        total_ops += 1
        lines.append(f"### {method} {path}")
        summ = clean(op.get("summary", ""), 100)
        desc = clean(op.get("description", ""), 220)
        head = f"`{op.get('operationId','')}`"
        if summ:
            head += f" — {summ}"
        lines.append(head)
        if desc and desc.rstrip("…") not in summ:
            lines.append(desc)
        params = (shared_params or []) + (op.get("parameters") or [])
        for loc in ("path", "query", "header"):
            ps = [p for p in params if p.get("in") == loc]
            if ps:
                bits = []
                for p in ps:
                    star = "*" if p.get("required") else ""
                    b = f"{p['name']}{star} ({typestr(p.get('schema', {}))})"
                    d = clean(p.get("description", ""), 90)
                    if d:
                        b += f" — {d}"
                    bits.append(b)
                lines.append(f"- {loc.capitalize()}: " + "; ".join(bits))
        rb = op.get("requestBody")
        if rb:
            content = rb.get("content", {})
            schema = (content.get("application/json") or next(iter(content.values()), {})).get("schema", {})
            name, resolved = deref(schema)
            req_flag = " (required)" if rb.get("required") else ""
            lines.append(f"- Body{req_flag}: {name or typestr(schema)}")
            lines += ["  " + l for l in schema_fields(resolved or schema)]
        lines.append(f"- Auth: {auth_str(op)}")
        lines.append(f"- Returns: {resp_str(op, used_schemas)}")
        lines.append("")
    if used_schemas:
        lines.append("## Response schemas")
        lines.append("")
        for name in sorted(used_schemas):
            s = schemas.get(name)
            if not s:
                continue
            lines.append(f"### {name}")
            fl = schema_fields(s)
            lines += fl if fl else [f"- ({typestr(s)})"]
            lines.append("")
    open(os.path.join(OUT, f"{fname}.md"), "w").write("\n".join(lines))

# flat index for grep-based routing
with open(os.path.join(OUT, "_index.md"), "w") as f:
    f.write("# Endpoint index — METHOD path → reference file\n\n")
    for path, method, fname, summ in sorted(index_rows):
        f.write(f"{method} {path} → {fname}.md — {summ}\n")

print(f"wrote {len(files)} reference files + _index.md, {total_ops} operations")
for fname in sorted(files):
    p = os.path.join(OUT, f"{fname}.md")
    print(f"  {fname}.md: {len(files[fname])} ops, {os.path.getsize(p)//1024}KB")
