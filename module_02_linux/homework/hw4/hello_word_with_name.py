"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""
from datetime import datetime
from flask import Flask

app = Flask(__name__)

Weekday_dict = {
    0: 'понедельника',
    1: 'вторника',
    2: 'среды',
    3: 'четверга',
    4: 'пятницы',
    5: 'субботы',
    6: 'воскресенья'
}


@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = Weekday_dict[datetime.today().weekday()]
    return f'Привет, {name}. Хорошего {weekday}!'


if __name__ == '__main__':
    app.run(debug=True)
