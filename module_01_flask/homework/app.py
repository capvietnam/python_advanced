import datetime
import os

from flask import Flask
import random
import re

app = Flask(__name__)

cars_str = ', '.join(['Chevrolet', 'Renault', 'Ford', 'Lada'])
cats_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
# TODO это  тоже две константы - имена констант пишутся большими буквами

words = None  # TODO переменные это основной код, расположите их после определения всех функций

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

counter_visits = 0  # TODO Аналогично предыдущему


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return {cars_str}


@app.route('/cats')
def cats():
    random_cat = random.choice(cats_list)
    return random_cat


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    global words
    if not words:
        with open(BOOK_FILE, encoding='utf-8') as file:
            book = file.read()
        words = re.findall(r'\w+', book.lower())
    random_word = random.choice(words)
    return random_word


@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return f'счётчик открытий: {counter_visits}'


if __name__ == '__main__':
    app.run(debug=True)
