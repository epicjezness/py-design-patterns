import logging

from .decorators import TitleDecorator
from .generators import NameGenerator
from ..base import StructuralDemoService

LOGGER = logging.getLogger(__name__)


class DecoratorStructuralDemoService(StructuralDemoService):
    """
    Class for demonstrating the decorator pattern.
    """

    _generator = NameGenerator
    _decorator = TitleDecorator

    def _create_generators_and_decorators(self) -> None:
        """
        Private method for setting up the generators and decorators.
        """

        LOGGER.info('Setting up generators and decorators.')
        self._generator = NameGenerator()
        self._decorator = TitleDecorator(self._generator)

    def _generate_names(self) -> None:
        """
        Private method for generating names using the NameGenerator object.
        """

        print(f'Generating names normally using generator: {self._generator.generate()}')

    def _generate_names_with_titles(self) -> None:
        """
        Private method for generating names with titles using the TitleDecorator object.
        """

        print(f'Generating names with titles using decorator: {self._decorator.generate()}')

    def execute(self) -> None:
        """
        Method for executing the demo routine of the decorator pattern.
          - Creates generators and decorators.
          - Generate names normally.
          - Generate names with titles.
        """

        LOGGER.info('Executing demo routine...')
        self._create_generators_and_decorators()
        self._generate_names()
        self._generate_names_with_titles()
        LOGGER.info('Demo routine Finished.')
