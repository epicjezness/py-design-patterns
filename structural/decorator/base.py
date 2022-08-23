from abc import ABC, abstractmethod


class Generator(ABC):
    """
    Abstract class for concrete Generator objects.
    """

    @abstractmethod
    def generate(self) -> str:
        """
        Abstract method for generating names.
        """

        raise NotImplementedError


class Decorator(Generator):
    """
    Base class for concrete Decorator objects.
    Follows the same interface as the Generator objects.
    Defines the wrapping interface for all concrete decorators.
    """

    _generator: Generator = None

    def __init__(self, generator: Generator) -> None:
        """
        Class constructor.

        :param generator: The generator object.
        """

        self._generator = generator

    @property
    def generator(self) -> Generator:
        return self._generator

    def generate(self) -> str:
        """
        Method for generating names.
        """

        return self._generator.generate()
