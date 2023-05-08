"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""


from typing import Collection, Type, Literal, Set
from types import TracebackType


class BlockErrors:
    def __init__(self, err_types: Set[Exception]):
        self.err_types = err_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if issubclass(exc_type, tuple(self.err_types)):  # TODO просто верните результат: return  issubclass(exc_type, tuple(self.err_types))
                return True
            else:
                return False
