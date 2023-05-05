"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app
import unittest
from unittest import TestCase

import unittest
from wtforms import ValidationError
from hw1_registration import RegistrationForm
from hw2_validators import number_length, NumberLength


class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    def test_email_field_valid(self):
        form = RegistrationForm(email='valid_email@example.com')
        self.assertTrue(form.email.validate(form))

    def test_email_field_invalid(self):
        form = RegistrationForm(email='invalid_email')
        self.assertFalse(form.email.validate(form))

    def test_email_validator_valid(self):
        validator = RegistrationForm().email.validators[1]
        validator('form', 'email@example.com')

    def test_email_validator_invalid(self):
        validator = RegistrationForm().email.validators[1]
        with self.assertRaises(ValidationError):
            validator('form', 'invalid_email')

    def test_phone_field_valid(self):
        form = RegistrationForm(phone='1234567')
        self.assertTrue(form.phone.validate(form))

    def test_phone_field_invalid(self):
        form = RegistrationForm(phone='123')
        self.assertFalse(form.phone.validate(form))

    def test_phone_validator_valid(self):
        validator = number_length(min=7, max=15, message='Invalid phone number')
        validator('form', '1234567')

    def test_phone_validator_invalid(self):
        validator = number_length(min=7, max=15, message='Invalid phone number')
        with self.assertRaises(ValidationError):
            validator('form', '123')

    def test_name_field_valid(self):
        form = RegistrationForm(name='John Doe')
        self.assertTrue(form.name.validate(form))

    def test_name_field_invalid(self):
        form = RegistrationForm(name='')
        self.assertFalse(form.name.validate(form))

    def test_address_field_valid(self):
        form = RegistrationForm(address='123 Main St')
        self.assertTrue(form.address.validate(form))

    def test_address_field_invalid(self):
        form = RegistrationForm(address='')
        self.assertFalse(form.address.validate(form))

    def test_index_field_valid(self):
        form = RegistrationForm(index=12345)
        self.assertTrue(form.index.validate(form))

    def test_index_field_invalid(self):
        form = RegistrationForm(index=-1)
        self.assertFalse(form.index.validate(form))

    def test_index_validator_valid(self):
        validator = RegistrationForm().index.validators[1]
        validator('form', '12345')

    def test_index_validator_invalid(self):
        validator = RegistrationForm().index.validators[1]
        with self.assertRaises(ValidationError):
            validator('form', '-1')


if __name__ == '__main__':
    unittest.main()
