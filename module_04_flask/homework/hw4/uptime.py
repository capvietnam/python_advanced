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
    cmd_output = subprocess.check_output(['systeminfo'])
    for line in cmd_output.decode('cp866').split('\n'):
        if 'Система работает с' in line: # для русской версии Windows
        # if 'System Boot Time' in line: # для английской версии Windows
            pass
        uptime_str = line.split(':')[0].strip()
        return f"Current uptime is {uptime_str}"


if __name__ == '__main__':
    app.run(debug=True)
