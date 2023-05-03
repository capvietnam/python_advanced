
from datetime import datetime
import unittest
from freezegun import freeze_time

from hello_word_with_day import app

GREETINGS = (
    'Хорошего понедельника',
    'Хорошего вторника',
    'Хорошей среды',
    'Хорошего четверга',
    'Хорошей пятницы',
    'Хорошей субботы',
    'Хорошего воскресенья'
)


class TestWeek(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_day_of_the_week_verification_test(self):
        name = 'jane'
        response = self.app.get(self.base_url + name)
        response_text = response.data.decode()
        correct_answer_str = f'Привет, {name}. {GREETINGS[datetime.today().weekday()]}!'
        self.assertTrue(correct_answer_str in response_text)

    @freeze_time('2022-02-23')
    def test_day_verification_test(self):
        name = 'jane'
        response = self.app.get(self.base_url + name)
        response_text = response.data.decode()
        correct_answer_str = f'Привет, {name}. Хорошей среды!'
        self.assertTrue(correct_answer_str in response_text)
