import logging

from .base import Factory
from .factory import GalaxyS22Factory, IPhoneFactory
from ..base import CreationalDemoService

LOGGER = logging.getLogger(__name__)


class FactoryMethodBehavioralDemoService(CreationalDemoService):
    """
    Class for demonstrating the factory method pattern.
    """

    _g_factory: GalaxyS22Factory
    _i_factory: IPhoneFactory

    def _setup_factories(self) -> None:
        """
        Private method for setting up the factories.
        """

        LOGGER.info('Setting up factories.')
        self._g_factory = GalaxyS22Factory()
        self._i_factory = IPhoneFactory()

    def _get_phones(self) -> None:
        """
        Private method for retrieving phone per declared factory.
        """

        self._get_phone_from_factory(self._g_factory)
        self._get_phone_from_factory(self._i_factory)

    @staticmethod
    def _get_phone_from_factory(factory: Factory) -> None:
        """
        Private static method for retrieving phone based on given factory.
        """

        LOGGER.info(f'Retrieving phone using {factory!r} factory.')
        LOGGER.info(factory.do_business_operation())

    def execute(self) -> None:
        """
        Method for executing the demo routine of the factory method pattern.
          - Setup the factories.
          - Get phones per factory.
        """

        LOGGER.info('Executing demo routine...')
        self._setup_factories()
        self._get_phones()
        LOGGER.info('Demo routine Finished.')
