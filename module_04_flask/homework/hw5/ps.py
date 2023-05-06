"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

import shlex
import subprocess
from flask import Flask, request


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args = request.args.getlist('arg')
    cmd = ['ps'] + [shlex.quote(arg) for arg in args]
    result = subprocess.check_output(cmd, universal_newlines=True)
    return f'<pre>{result}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
