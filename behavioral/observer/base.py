from abc import ABCMeta, abstractmethod


class Publisher(metaclass=ABCMeta):
    """
    The Publisher interface.
    Declares a set of methods for managing observers.
    """

    @abstractmethod
    def _notify(self) -> None:
        """
        Abstract method for notifying all observers about an event.
        """
        raise NotImplementedError

    @abstractmethod
    def subscribe(self, subscriber: 'Subscriber') -> None:
        """
        Abstract method for subscribing an observer into the publisher.
        """
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self, subscriber: 'Subscriber') -> None:
        """
        Abstract method for unsubscribing an observer from the publisher.
        """
        raise NotImplementedError

    @abstractmethod
    def unsubscribe_all(self) -> None:
        """
        Abstract method for unsubscribing all observers from the publisher.
        """
        raise NotImplementedError

    @abstractmethod
    def update_state(self) -> None:
        """
        Abstract method for toggling the object's state.
        """
        raise NotImplementedError


class Subscriber(metaclass=ABCMeta):
    """
    The Subscriber interface.
    Declares the update method that is used by Publisher objects.
    """

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        """
        Abstract method for receiving updates from an observed Publisher object.

        :param publisher: The observed Publisher object.
        """
        raise NotImplementedError
