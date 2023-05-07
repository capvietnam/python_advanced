import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_ignoring_errors(self):
        # Test ignoring errors
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0
            b = 1 + '1'
        self.assertTrue(True)

    def test_propogate_errors(self):
        # Test propogate errors
        err_types = {ZeroDivisionError}
        with self.assertRaises(TypeError):
            with BlockErrors(err_types):
                a = 1 / '0'

    def test_inner_block_ignores_error(self):
        # Test inner block ignores error
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / '0'
            self.assertTrue(True)

    def test_ignoring_child_exceptions(self):
        # Test ignoring child exceptions
        err_types = {Exception}
        with BlockErrors(err_types):
            try:
                a = 1 / '0'
            except TypeError:
                pass
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
