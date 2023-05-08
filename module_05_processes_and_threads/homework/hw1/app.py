"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
import os
import subprocess
from typing import List
from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError("Port must be an integer")

    # Выполняем команду lsof для получения списка процессов по порту
    command = subprocess.Popen(["lsof", "-i", f":{port}"], stdout=subprocess.PIPE)
    # Считываем вывод команды в байтовом формате
    output = command.stdout.read()
    # Декодируем вывод в строку
    output = output.decode("utf-8")
    # Разбиваем вывод на строки
    lines = output.split("\n")

    # Из каждой строки получаем PID процесса и добавляем в список
    pids = []
    for line in lines:
        if "LISTEN" in line:
            parts = line.split()
            # Первый элемент в строке содержит PID
            pid = int(parts[1])
            pids.append(pid)

    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    for pid in pids:
        os.kill(pid, 9)
    return run_server(5000)


def run_server(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    if get_pids(port):
        free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run_server(5000)
