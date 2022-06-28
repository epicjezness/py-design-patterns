import logging

from .base import Publisher, Subscriber

LOGGER = logging.getLogger(__name__)


class ConcreteASubscriber(Subscriber):
    """
    Concrete Subscriber class for observing a Publisher object.
    """

    def update(self, publisher: Publisher) -> None:
        """
        Method for receiving updates from an observed Publisher object.

        :param publisher: The observed Publisher object.
        """

        LOGGER.info(f'Received from observed object: State updated to {publisher.state}')


class ConcreteBSubscriber(Subscriber):
    """
    Concrete Subscriber class for observing a Publisher object.
    """

    def update(self, publisher: Publisher) -> None:
        """
        Method for receiving updates from an observed Publisher object.

        :param publisher: The observed Publisher object.
        """

        LOGGER.info(f'Received from observed object: State updated to {publisher.state}')


class ConcreteCSubscriber(Subscriber):
    """
    Concrete Subscriber class for observing a Publisher object.
    """

    def update(self, publisher: Publisher) -> None:
        """
        Method for receiving updates from an observed Publisher object.

        :param publisher: The observed Publisher object.
        """

        LOGGER.info(f'Received from observed object: State updated to {publisher.state}')
