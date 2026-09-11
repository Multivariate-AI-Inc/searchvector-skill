import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SV_API = ROOT / "scripts" / "sv_api.py"


def sample_schema():
    return {
        "openapi": "3.0.3",
        "paths": {
            "/api/public/": {
                "get": {
                    "operationId": "public_list",
                    "summary": "List public resources",
                    "tags": ["Public API"],
                    "security": [{"BearerAuth": []}, {"imperson" + "ationCookieAuth": []}],
                    "responses": {"200": {"description": "OK"}},
                }
            },
            "/api/old/": {
                "get": {
                    "operationId": "old_list",
                    "summary": "List old resources",
                    "tags": ["Public API"],
                    "deprecated": True,
                    "responses": {"200": {"description": "OK"}},
                }
            },
            "/api/private/": {
                "get": {
                    "operationId": "private_list",
                    "summary": "List " + "in" + "ternal resources",
                    "tags": ["In" + "ternal APIs"],
                    "responses": {"200": {"description": "OK"}},
                }
            },
        },
    }


class SearchVectorApiCliTest(unittest.TestCase):
    def run_cli(self, *args, env=None):
        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)
        return subprocess.run(
            [sys.executable, str(SV_API), *args],
            cwd=ROOT,
            env=merged_env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def with_schema_cache(self):
        tempdir = tempfile.TemporaryDirectory()
        cache = Path(tempdir.name) / "schema.json"
        cache.write_text(json.dumps(sample_schema()), encoding="utf-8")
        return tempdir, {"SEARCHVECTOR_SCHEMA_CACHE": str(cache)}

    def test_search_hides_deprecated_and_private_operations_by_default(self):
        tempdir, env = self.with_schema_cache()
        self.addCleanup(tempdir.cleanup)

        result = self.run_cli("search", "list", env=env)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("/api/public/", result.stdout)
        self.assertNotIn("/api/old/", result.stdout)
        self.assertNotIn("/api/private/", result.stdout)

    def test_show_filters_non_public_security_schemes(self):
        tempdir, env = self.with_schema_cache()
        self.addCleanup(tempdir.cleanup)

        result = self.run_cli("show", "public_list", env=env)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("BearerAuth", result.stdout)
        self.assertNotIn("imperson" + "ation", result.stdout)

    def test_validate_rejects_forbidden_public_terms(self):
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            (root / "references").mkdir()
            (root / "scripts").mkdir()
            (root / "SKILL.md").write_text("ok", encoding="utf-8")
            (root / "README.md").write_text("ok", encoding="utf-8")
            (root / "references" / "_index.md").write_text("GET /api/x/ -> misc.md\n", encoding="utf-8")
            (root / "references" / "misc.md").write_text("stag" + "ing", encoding="utf-8")
            (root / "scripts" / "sv_api.py").write_text("", encoding="utf-8")

            result = self.run_cli("validate", "--root", str(root))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("forbidden public term", result.stderr)


if __name__ == "__main__":
    unittest.main()
