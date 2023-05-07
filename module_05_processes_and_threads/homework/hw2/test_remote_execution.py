import unittest
from remote_execution import run_python_code_in_subprocess


class TestRunPythonCodeInSubprocess(unittest.TestCase):

    def test_returns_stdout_and_stderr(self):
        code = "print('hello')\nprint('world')"
        timeout = 10
        stdout, stderr, killed = run_python_code_in_subprocess(code, timeout)
        self.assertEqual(stdout, "hello\nworld\n")
        self.assertEqual(stderr, "")
        self.assertEqual(killed, False)

    def test_returns_stderr_on_syntax_error(self):
        code = "print('hello' +)\nprint('world')"
        timeout = 10
        stdout, stderr, killed = run_python_code_in_subprocess(code, timeout)
        self.assertEqual(stdout, "")
        self.assertIn("SyntaxError", stderr)
        self.assertEqual(killed, False)

    def test_kills_process_on_timeout(self):
        code = "while True: pass"
        timeout = 1
        stdout, stderr, killed = run_python_code_in_subprocess(code, timeout)
        self.assertEqual(stdout, "")
        self.assertEqual(stderr, "")
        self.assertEqual(killed, True)


if __name__ == '__main__':
    unittest.main()
