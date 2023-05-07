import sys
import io
import unittest
from redirect import Redirect


class TestRedirect(unittest.TestCase):
    def test_stdout_redirect(self):
        stdout_file = io.StringIO()
        with Redirect(stdout=stdout_file):
            print('Hello stdout')
            print('Hello again stdout')
        self.assertEqual(stdout_file.getvalue(), 'Hello stdout\nHello again stdout\n')

    def test_stderr_redirect(self):
        stderr_file = io.StringIO()
        with Redirect(stderr=stderr_file):
            try:
                print('Hello stderr', file=sys.stderr)
                raise ValueError('Hello error')
            except ValueError:
                pass
        self.assertIn('Hello stderr', stderr_file.getvalue())
        self.assertRegex(stderr_file.getvalue(), r'Hello stderr')

    def test_stdout_stderr_redirect(self):
        stdout_file = io.StringIO()
        stderr_file = io.StringIO()
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout')
            print('Hello stderr', file=sys.stderr)
            try:
                raise ValueError('Hello error')
            except ValueError:
                pass
        self.assertEqual(stdout_file.getvalue(), 'Hello stdout\n')
        self.assertIn('Hello stderr', stderr_file.getvalue())
        self.assertRegex(stderr_file.getvalue(), r'Hello stderr')


if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
