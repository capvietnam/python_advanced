"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        app.config["WTF_CSRF_ENABLED"] = False

    def tearDown(self):
        pass

    def test_valid_email_phone_name_address_index(self):
        # Тест для проверки корректности валидации email адреса

        # Данные для тестового запроса
        data = {
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': 'Test Address',
            'index': 12345,
            'comment': 'Test comment',
        }

        # Отправляем запрос на endpoint с валидными данными
        response = self.test_client.post('/registration', json=data)

        # Убеждаемся, что ответ сервера - успешная регистрация
        self.assertIn(b'Successfully registered user test@example.com with phone +71234567890', response.data)

    def test_invalid_email(self):
        # Тест для проверки невалидного email адреса

        # Данные для тестового запроса с невалидным email адресом
        data = {
            'email': 'invalid email',
            'phone': 1234567890,
            'name': 'Test User',
            'address': 'Test Address',
            'index': 12345,
            'comment': 'Test comment'
        }

        # Отправляем запрос на endpoint с невалидным email адресом
        response = self.test_client.post('/registration', json=data)

        # Ожидаем ошибку в ответе сервера, так как email адрес невалидный
        self.assertIn(b"Invalid input, {'email': ['Invalid email format']}", response.data)

    def test_invalid_phone(self):
        # Тест для проверки корректности валидации email адреса

        # Данные для тестового запроса
        data = {
            'email': 'test@example.com',
            'phone': 12345678900,
            'name': 'Test User',
            'address': 'Test Address',
            'index': 12345,
            'comment': 'Test comment',
        }

        # Отправляем запрос на endpoint с валидными данными
        response = self.test_client.post('/registration', json=data)

        # Убеждаемся, что ответ сервера - успешная регистрация
        self.assertIn(b"Invalid input, {'phone': ['Invalid phone number']}", response.data)

    def test_no_name(self):
        # Тест для проверки корректности валидации email адреса

        # Данные для тестового запроса
        data = {
            'email': 'test@example.com',
            'phone': 1234567890,
            'address': 'Test Address',
            'index': 12345,
            'comment': 'Test comment',
        }

        # Отправляем запрос на endpoint с валидными данными
        response = self.test_client.post('/registration', json=data)

        # Убеждаемся, что ответ сервера - успешная регистрация
        self.assertIn(b"Invalid input, {'name': ['This field is required.']}", response.data)

    def test_no_address(self):
        # Тест для проверки корректности валидации email адреса

        # Данные для тестового запроса
        data = {
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'index': 12345,
            'comment': 'Test comment',
        }

        # Отправляем запрос на endpoint с валидными данными
        response = self.test_client.post('/registration', json=data)

        # Убеждаемся, что ответ сервера - успешная регистрация
        self.assertIn(b"Invalid input, {'address': ['This field is required.']}", response.data)

    def test_invalid_index(self):
        # Тест для проверки корректности валидации email адреса

        # Данные для тестового запроса
        data = {
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': 'Test Address',
            'index': 'y',
            'comment': 'Test comment',
        }

        # Отправляем запрос на endpoint с валидными данными
        response = self.test_client.post('/registration', json=data)

        # Убеждаемся, что ответ сервера - успешная регистрация
        self.assertIn(b"Invalid input, {'index': ['Not a valid integer value.', 'Invalid index']}", response.data)


if __name__ == '__main__':
    unittest.main()
