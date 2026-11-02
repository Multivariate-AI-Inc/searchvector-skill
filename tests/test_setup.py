import argparse
import contextlib
import importlib.util
import io
import json
import os
import shlex
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sv_api_setup_tests', Path(__file__).resolve().parents[1] / 'scripts/sv_api.py')
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class TokenSetupTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.env = patch.dict(os.environ, {'XDG_CONFIG_HOME': self.temp.name}, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)
        self.path = Path(self.temp.name) / 'searchvector' / 'credentials.json'

    def setup_token(self, value='sample-secret', browser=True):
        output = io.StringIO()
        with patch.object(api.sys.stdin, 'isatty', return_value=True), patch.object(api.getpass, 'getpass', return_value=value), patch.object(api.webbrowser, 'open', return_value=browser), contextlib.redirect_stdout(output):
            api.cmd_setup(argparse.Namespace(no_browser=False))
        return output.getvalue()

    def test_setup_saves_private_credentials_and_api_reads_them(self):
        output = self.setup_token()
        self.assertNotIn('sample-secret', output)
        self.assertEqual(self.path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(self.path.parent.stat().st_mode & 0o777, 0o700)
        self.assertEqual(api.auth_headers(), {'Authorization': 'Token sample-secret'})
        self.setup_token('replacement')
        self.assertEqual(api.auth_headers(), {'Authorization': 'Token replacement'})

    def test_environment_credentials_override_saved_token(self):
        self.setup_token()
        with patch.dict(os.environ, {'SEARCHVECTOR_JWT': 'jwt-value'}):
            self.assertEqual(api.auth_headers(), {'Authorization': 'Bearer jwt-value'})
        with patch.dict(os.environ, {'SEARCHVECTOR_API_TOKEN': 'env-value'}):
            self.assertEqual(api.auth_headers(), {'Authorization': 'Token env-value'})

    def test_empty_or_invalid_input_preserves_existing_token(self):
        self.setup_token()
        for value in ['', '   ', 'bad\nheader', 'bad token']:
            with self.subTest(value=value), self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                self.setup_token(value)
            self.assertEqual(api.auth_headers(), {'Authorization': 'Token sample-secret'})

    def test_browser_failure_still_allows_setup(self):
        output = self.setup_token(browser=False)
        self.assertIn('https://searchvector.io/dashboard/api-token', output)
        self.assertEqual(api.auth_headers(), {'Authorization': 'Token sample-secret'})

    def test_noninteractive_setup_fails_without_saving(self):
        with patch.object(api.sys.stdin, 'isatty', return_value=False), self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            api.cmd_setup(argparse.Namespace(no_browser=True))
        self.assertFalse(self.path.exists())

    def test_hidden_prompt_unavailable_does_not_fall_back_to_echo(self):
        import warnings
        with patch.object(api.sys.stdin, 'isatty', return_value=True), patch.object(api.getpass, 'getpass', side_effect=api.getpass.GetPassWarning('unavailable')), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            api.cmd_setup(argparse.Namespace(no_browser=True))
        self.assertFalse(self.path.exists())

    def test_corrupt_saved_file_has_actionable_error_without_contents(self):
        self.path.parent.mkdir()
        self.path.write_text('secret-invalid-json')
        output = io.StringIO()
        with contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            api.auth_headers()
        self.assertIn('setup', output.getvalue())
        self.assertNotIn('secret-invalid-json', output.getvalue())

    def test_launcher_passes_literal_paths_and_configuration_to_macos_terminal(self):
        script = Path(self.temp.name) / "folder with spaces" / "token's $(literal).py"
        with patch.object(api.sys, 'platform', 'darwin'), patch.object(api, '__file__', str(script)), patch.object(api.subprocess, 'run') as run, contextlib.redirect_stdout(io.StringIO()):
            api.cmd_setup(argparse.Namespace(launch=True, no_browser=True))
        command = run.call_args.args[0]
        self.assertEqual(command[0], 'osascript')
        self.assertEqual(shlex.split(command[-1]), ['env', 'XDG_CONFIG_HOME=' + self.temp.name, api.sys.executable, str(script.resolve()), 'setup', '--no-browser'])
        self.assertIn('on run argv', command[2])
        self.assertFalse(self.path.exists())

    def test_linux_launcher_opens_terminal_without_reading_token(self):
        with patch.dict(os.environ, {'DISPLAY': ':0'}), patch.object(api.sys, 'platform', 'linux'), patch.object(api.shutil, 'which', side_effect=lambda name: '/usr/bin/xterm' if name == 'xterm' else None), patch.object(api.subprocess, 'Popen') as launch, contextlib.redirect_stdout(io.StringIO()):
            api.cmd_setup(argparse.Namespace(launch=True, no_browser=False))
        command = launch.call_args.args[0]
        self.assertEqual(command[:2], ['/usr/bin/xterm', '-e'])
        self.assertIn('setup', command)
        self.assertNotIn('--launch', command)
        self.assertFalse(self.path.exists())

    def test_launcher_failure_provides_manual_fallback(self):
        output = io.StringIO()
        with patch.object(api.sys, 'platform', 'linux'), patch.object(api.shutil, 'which', return_value=None), contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            api.cmd_setup(argparse.Namespace(launch=True, no_browser=False))
        self.assertIn('setup', output.getvalue())
        self.assertIn('terminal', output.getvalue())

    def test_macos_launch_denied_reports_fallback_without_details(self):
        output = io.StringIO()
        with patch.object(api.sys, 'platform', 'darwin'), patch.object(api.subprocess, 'run', side_effect=api.subprocess.CalledProcessError(1, 'osascript', stderr='private-details')), contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            api.cmd_setup(argparse.Namespace(launch=True, no_browser=False))
        self.assertIn('terminal', output.getvalue())
        self.assertNotIn('private-details', output.getvalue())

    def test_headless_linux_reports_manual_fallback(self):
        output = io.StringIO()
        with patch.object(api.sys, 'platform', 'linux'), patch.object(api.shutil, 'which', return_value='/usr/bin/xterm'), contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            api.cmd_setup(argparse.Namespace(launch=True, no_browser=False))
        self.assertIn('setup', output.getvalue())
        self.assertFalse(self.path.exists())

    def test_auth_status_never_prints_token(self):
        self.setup_token()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            api.cmd_auth_status(argparse.Namespace())
        self.assertIn('configured', output.getvalue())
        self.assertNotIn('sample-secret', output.getvalue())

    def test_missing_credentials_points_to_setup(self):
        output = io.StringIO()
        with contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            api.auth_headers()
        self.assertIn('setup', output.getvalue())


if __name__ == '__main__':
    unittest.main()
