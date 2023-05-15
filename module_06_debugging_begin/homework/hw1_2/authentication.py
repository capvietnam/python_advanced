"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""
import flask
import getpass
import hashlib
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

logger = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
logger.setLevel(logging.INFO)
app.logger.addHandler(logger)


def is_strong_password(password: str) -> bool:
    return True


def input_and_check_password() -> bool:
    app.logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        app.logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        app.logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        app.logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    app.logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    app.logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
