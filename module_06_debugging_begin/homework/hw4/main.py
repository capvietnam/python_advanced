"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
import os
import shlex
import subprocess
from itertools import groupby
from typing import Dict


def task1() -> Dict[str, int]:
    level_count = {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
    with open('skillbox_json_messages.log', 'r') as file:
        for line in file:
            for level in level_count.keys():
                if level in line:
                    level_count[level] += 1
    return level_count


def task2() -> int:
    all_level_count = {}
    with open('skillbox_json_messages.log', 'r') as file:
        for line in file:
            line = json.loads(line)
            time = line['time'][0: 2]
            if time in all_level_count.keys():
                all_level_count[time] += 1
            else:
                all_level_count[time] = 0
    return max(all_level_count, key=all_level_count.get)


def task3() -> int:
    count_CRITICAL_5_00_5_20 = 0
    all_CRITICAL = subprocess.Popen(["grep", '"level": "CRITICAL"', f"skillbox_json_messages.log"],
                                    stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', '-c', '"time": "05:[0,1]'], stdin=all_CRITICAL.stdout,
                            stdout=subprocess.PIPE).stdout.read().decode("utf-8")[:-1]
    return grep


def task4() -> int:
    """
    Если имеется ввиду и множественное число
    """
    mess_dog = subprocess.Popen(["grep", "-c", "-w", 'dog', f"skillbox_json_messages.log"],
                                stdout=subprocess.PIPE).stdout.read().decode("utf-8")[:-1]
    return mess_dog


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    with open('skillbox_json_messages.log', 'r') as file:
        lines = str(file.readlines())
        lines = json.load(file)
        print(type(lines))
    return 0


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')

