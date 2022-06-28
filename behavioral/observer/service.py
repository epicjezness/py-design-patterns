import logging

from .publisher import ConcretePublisher
from .subscribers import ConcreteASubscriber, ConcreteBSubscriber, ConcreteCSubscriber
from ..base import BehavioralDemoService

LOGGER = logging.getLogger(__name__)


class ObserverBehavioralDemoService(BehavioralDemoService):
    """
    Class for demonstrating the observer pattern.
    """

    publisher: ConcretePublisher

    def __init__(self):
        """
        Class constructor.
        """

        self.publisher = ConcretePublisher()

    def _add_subscribers(self) -> None:
        """
        Private method for adding subscribers to the publisher object.
        :return:
        """

        LOGGER.info('Removing existing subscribers.')
        self.publisher.unsubscribe_all()

        LOGGER.info('Adding new subscribers.')
        subs = [ConcreteASubscriber(), ConcreteBSubscriber(), ConcreteCSubscriber()]

        for sub in subs:
            self.publisher.subscribe(sub)

    def _update_publisher_state(self) -> None:
        """
        Private method for updating the publisher's state.
        """

        LOGGER.info('Updating Publisher state.')
        self.publisher.update_state()

    def execute(self) -> None:
        """
        Method for executing the demo routine of the observer pattern.
          - Removes existing subscribers if existing.
          - Populates and adds subscribers to the publisher.
          - Updates the publisher's state.
        """

        LOGGER.info('Executing demo routine...')
        LOGGER.info(f'Publisher object state: {self.publisher.state}')
        self._add_subscribers()
        self._update_publisher_state()
        LOGGER.info(f'Publisher object state: {self.publisher.state}')
        LOGGER.info('Demo routine Finished.')
