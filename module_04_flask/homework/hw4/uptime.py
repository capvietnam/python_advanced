"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/uptime')
def uptime():
    cmd_output = subprocess.check_output(['uptime'])
    uptime_str = cmd_output.decode().split('up ')[0].split(',')[0]  # получаем первую часть строки
    return f"Current uptime is {uptime_str}"


if __name__ == '__main__':
    app.run(debug=True)
