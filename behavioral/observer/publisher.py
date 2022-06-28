from typing import List

from .base import Publisher, Subscriber


class ConcretePublisher(Publisher):
    """
    Concrete Publisher class for notifying registered observers to any changes in the object's state.
    """

    _subscribers: List['Subscriber']
    state: bool = False

    def _notify(self) -> None:
        """
        Private method for notifying all observers about an event.
        """

        for sub in self._subscribers:
            sub.update(self)

    def subscribe(self, subscriber: Subscriber) -> None:
        """
        Method for subscribing an observer into the publisher.

        :param subscriber: The Subscriber object.
        """

        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        """
        Method for unsubscribing an observer from the publisher.

        :param subscriber: The Subscriber object.
        """

        self._subscribers.append(subscriber)

    def unsubscribe_all(self) -> None:
        """
        Method for unsubscribing all observers from the publisher.
        """

        self._subscribers = []

    def update_state(self) -> None:
        """
        Method for toggling the object's state.
        """

        self.state = not self.state
        self._notify()
