#!/usr/bin/env python3
"""Safe SearchVector API client. Auth is read from env — the token is never
printed, logged, or accepted as an argument (so it can't leak into shell
history or agent transcripts).

Env:
  SEARCHVECTOR_API_TOKEN  -> Authorization: Token <key>   (scripts/integrations)
  SEARCHVECTOR_JWT        -> Authorization: Bearer <jwt>  (used if API token unset)
  SEARCHVECTOR_BASE_URL   -> default https://searchvector.io

Usage:
  python sv_request.py GET /api/projects/
  python sv_request.py GET /api/projects/ -q search=nike -q page=2
  python sv_request.py POST /api/projects/ -d '{"name":"My Site","website_url":"https://example.com"}'
  echo '{"name":"X"}' | python sv_request.py POST /api/projects/ -d @-
"""
import argparse, json, os, sys, urllib.error, urllib.parse, urllib.request

def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"])
    ap.add_argument("path", help="API path, e.g. /api/projects/ (trailing slash matters)")
    ap.add_argument("-q", "--query", action="append", default=[], metavar="key=value")
    ap.add_argument("-d", "--data", help="JSON body, or @- to read from stdin, or @file.json")
    args = ap.parse_args()

    token = os.environ.get("SEARCHVECTOR_API_TOKEN")
    jwt = os.environ.get("SEARCHVECTOR_JWT")
    if not token and not jwt:
        sys.exit("error: set SEARCHVECTOR_API_TOKEN (or SEARCHVECTOR_JWT) in your environment first.\n"
                 "  export SEARCHVECTOR_API_TOKEN=...   # add to ~/.zshrc or a gitignored .env")
    auth = f"Token {token}" if token else f"Bearer {jwt}"

    base = os.environ.get("SEARCHVECTOR_BASE_URL", "https://searchvector.io").rstrip("/")
    if not args.path.startswith("/"):
        sys.exit("error: path must start with /api/...")
    url = base + args.path
    if args.query:
        url += "?" + urllib.parse.urlencode(dict(q.split("=", 1) for q in args.query))

    body = None
    if args.data is not None:
        raw = sys.stdin.read() if args.data == "@-" else (
            open(args.data[1:]).read() if args.data.startswith("@") else args.data)
        try:
            body = json.dumps(json.loads(raw)).encode()  # validate JSON before sending
        except json.JSONDecodeError as e:
            sys.exit(f"error: body is not valid JSON: {e}")

    # The server rejects requests without a browser-like User-Agent — always send one.
    ua = os.environ.get("SEARCHVECTOR_USER_AGENT",
                        "Mozilla/5.0 (compatible; searchvector-client/1.0)")
    req = urllib.request.Request(url, data=body, method=args.method, headers={
        "Authorization": auth, "Content-Type": "application/json",
        "Accept": "application/json", "User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"HTTP {r.status}", file=sys.stderr)
            out = r.read().decode()
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}", file=sys.stderr)
        out = e.read().decode()
        try:
            print(json.dumps(json.loads(out), indent=2))
        except ValueError:
            print(out[:2000])
        sys.exit(1)
    try:
        print(json.dumps(json.loads(out), indent=2))
    except ValueError:
        print(out[:2000])

if __name__ == "__main__":
    main()
