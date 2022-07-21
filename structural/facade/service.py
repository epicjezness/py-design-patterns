import logging

from .facade import PersonFacade
from ..base import StructuralDemoService

LOGGER = logging.getLogger(__name__)


class FacadeBehavioralDemoService(StructuralDemoService):
    """
    Class for demonstrating the facade pattern.
    """

    _facade: PersonFacade = None

    def _create_facade(self) -> None:
        """
        Private method for creating the facade object.
        """

        LOGGER.info('Creating facade...')
        self._facade = PersonFacade()

    def _generate_person(self) -> None:
        """
        Private method for generating person object.
        """

        LOGGER.info('Generating person...')

        person = self._facade.generate_person()
        LOGGER.info(f'Output: {person}')

    def execute(self) -> None:
        """
        Method for executing the demo routine of the facade pattern.
          - Creates the facade.
          - Generate the person.
        """

        LOGGER.info('Executing demo routine...')
        self._create_facade()
        self._generate_person()
        LOGGER.info('Demo routine Finished.')
