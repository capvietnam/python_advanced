import unittest
from decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_no_dot(self):
        self.assertEqual(decrypt('абра-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('.'), '')

    def test_one_dot(self):
        self.assertEqual(decrypt('abra-kadabra.'), 'abra-kadabra')
        self.assertEqual(decrypt('abraa..-.kadabra'), 'abra-kadabra')
        self.assertEqual(decrypt('abrau...-kadabra'), 'abra-kadabra')

    def test_two_dot(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')

    def test_three_dot(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('1..2.3'), '23')

    def test_many_dot(self):
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('абр......a.'), 'a')
        self.assertEqual(decrypt('1.......................'), '')


if __name__ == '__main__':
    unittest.main()
