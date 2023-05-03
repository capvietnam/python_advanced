import unittest
from person import Person


class TestDecrypt(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.person = Person('Alex', 1990, 'Moscow')

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 33)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'Alex')

    def test_set_name(self):
        self.person.set_name('Kate')
        self.assertEqual(self.person.get_name(), 'Kate')

    def test_set_address(self):
        self.person.set_address('Paris')
        self.assertEqual(self.person.get_address(), 'Paris')

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), 'Moscow')

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())
        homeless_person = Person('Tom', 2000)
        self.assertTrue(homeless_person.is_homeless())

if __name__ == '__main__':
    unittest.main()
