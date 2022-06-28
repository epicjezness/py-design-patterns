from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    """
    The Mediator interface.
    Declares a method used by components to notify the mediator about various events.
    The Mediator may react to these events and pass the execution to other components.
    """

    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        """
        Abstract method for notifying the Mediator and react based on the given event.

        :param sender: The sender object.
        :param event: The event object.
        """

        raise NotImplementedError


class Component(object):
    """
    Base class for Component objects.
    Provides the basic functionality of storing a mediator's instance inside Component objects.
    """

    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator
