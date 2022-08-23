from random import choice
from typing import List

from .base import Generator


class NameGenerator(Generator):
    """
    Generator for generating names.
    """

    _names: List[str]

    def __init__(self):
        """
        Class constructor
        """

        self._names = [
            'Alex',
            'Charlie',
            'Jessie',
            'Kerry',
            'Sydney'
        ]

    def generate(self) -> str:
        """
        Method for generating names.
        """

        return choice(self._names)
