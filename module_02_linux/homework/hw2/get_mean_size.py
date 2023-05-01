"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(lines: str) -> float:
    sizes = []
    for line in lines:
        if line[0] == '-':
            parts = line.split()
            if len(parts) >= 5:
                try:
                    size = int(parts[4])
                    sizes.append(size)
                except ValueError:
                    pass
    if sizes:
        return sum(sizes) / len(sizes)
    else:
        return 0


if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    print(get_mean_size(lines))
