import logging

from .obj import SingletonObject
from ..base import CreationalDemoService

LOGGER = logging.getLogger(__name__)


class SingletonCreationalDemoService(CreationalDemoService):
    """
    Class for demonstrating the singleton pattern.
    """

    _s1: SingletonObject
    _s2: SingletonObject

    def _setup_singleton_objects(self) -> None:
        """
        Private method for setting up the singleton objects.
        """

        LOGGER.info('Setting up singleton objects.')
        self._s1 = SingletonObject()
        self._s2 = SingletonObject()

    def _check_singleton_instance(self) -> None:
        """
        Private method for checking if all singleton objects are the same object.
        By using id built-in function, which is an object's unique ID assigned upon creation, we can determine if the
        singleton objects are the same instance.
        """

        print(f'Check if same instance: {id(self._s1)} == {id(self._s2)}')

        if id(self._s1) == id(self._s2):
            print("Singleton objects are the SAME instance")
        else:
            print("Singleton objects are DIFFERENT instances.")

    def execute(self) -> None:
        """
        Method for executing the demo routine of the singleton pattern.
          - Setup the singleton objects.
          - Check if singleton objects are the same instance.
        """

        LOGGER.info('Executing demo routine...')
        self._setup_singleton_objects()
        self._check_singleton_instance()
        LOGGER.info('Demo routine Finished.')
