import unittest
from decrypt import decrypt

TestAnswer0 = {'абра-кадабра': 'абра-кадабра', '.': ''}
TestAnswer1 = {'abra-kadabra.': 'abra-kadabra', 'abraa..-.kadabra': 'abra-kadabra', 'abrau...-kadabra': 'abra-kadabra'}
TestAnswer2 = {'абраа..-кадабра': 'абра-кадабра', 'абра--..кадабра': 'абра-кадабра'}
TestAnswer3 = {'абраа..-.кадабра': 'абра-кадабра', 'абрау...-кадабра': 'абра-кадабра', '1..2.3': '23'}
TestAnswerMany = {'абра........': '', 'абр......a.': 'a', '1.......................': ''}


class TestDecrypt(unittest.TestCase):

    def test_no_dot(self):
        for key, value in TestAnswer0.items():
            self.assertEqual(decrypt(key), value)

    def test_one_dot(self):
        for key, value in TestAnswer1.items():
            self.assertEqual(decrypt(key), value)

    def test_two_dot(self):
        for key, value in TestAnswer2.items():
            self.assertEqual(decrypt(key), value)

    def test_three_dot(self):
        for key, value in TestAnswer3.items():
            self.assertEqual(decrypt(key), value)

    def test_many_dot(self):
        for key, value in TestAnswerMany.items():
            self.assertEqual(decrypt(key), value)

if __name__ == '__main__':
    unittest.main()
