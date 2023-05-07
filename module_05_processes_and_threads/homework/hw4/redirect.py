"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

import sys
from typing import IO, Optional
from io import StringIO


class Redirect:
    def __init__(self, stdout: Optional[IO] = None, stderr: Optional[IO] = None):
        self.stdout = stdout or StringIO()
        self.stderr = stderr or StringIO()

    def __enter__(self):
        self.stdout_replaced = sys.stdout
        self.stderr_replaced = sys.stderr
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout_replaced
        sys.stderr = self.stderr_replaced
        if exc_type:
            # если произошла ошибка, то нужно вывести traceback
            print(exc_type, exc_val, exc_tb, file=self.stderr)


