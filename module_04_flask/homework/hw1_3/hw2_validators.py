"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, ValidationError
from typing import Optional



def number_length(min_: int, max_: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        number = str(field.data)
        if not min_ <= len(number) <= max_:
            if message is not None:
                raise ValidationError(message)
            else:
                raise ValidationError(f'Number should have length between {min_} and {max_}.')
    return _number_length


class NumberLength:
    def init(self, min_: int, max_: int, message: Optional[str] = None):
        # TODO этот и следующий методы должны иметь в имени двойное подчеркивание до и после имени
        self.min_ = min_
        self.max_ = max_
        self.message = message

    def call(self, form: FlaskForm, field: Field):
        number = str(field.data)
        if not self.min_ <= len(number) <= self.max_:
            if self.message is not None:
                raise ValidationError(self.message)
            else:
                raise ValidationError(f'Number should have length between {self.min_} and {self.max_}.')