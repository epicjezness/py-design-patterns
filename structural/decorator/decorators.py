from random import choice
from typing import List

from .base import Decorator, Generator


class TitleDecorator(Decorator):
    """
    Decorator that appends titles to generated names.
    """

    _titles: List[str]

    def __init__(self, generator: Generator):
        super().__init__(generator)

        self._titles = [
            'Dr.',
            'Hon.',
            'Mr.',
            'Mrs.',
            'Ms.',
            'Prof.',
            'Rev.',
            'Sir'
        ]

    def generate(self) -> str:
        """
        Method for generating names.
        Decorators may call parent implementation of the operation, instead of calling the wrapped object directly.
        This approach simplifies extension of decorator classes.
        """

        return self._prepend_title(super().generate())

    def _prepend_title(self, name: str) -> str:
        """
        Method for prepending titles to generated names.
        """

        return f'{choice(self._titles)} {name}'
