from .base import Mediator
from .units import AirForce, Army, Navy


class CommunicationsRelay(Mediator):
    """
    Concrete Mediator class
    """

    def __init__(self, army: Army, navy: Navy, af: AirForce) -> None:
        """
        Class constructor.

        :param army: The Army object.
        :param navy: The Navy object.
        :param af: The AirForce object.
        """

        self._army = army
        self._navy = navy
        self._af = af

        self._army.mediator = self
        self._navy.mediator = self
        self._af.mediator = self

    def notify(self, sender: object, event: str) -> None:
        """
        Method for notifying the Mediator and react based on the given event.

        :param sender: The sender object.
        :param event: The event object.
        """

        if event == "G_I":
            self._army.do_interception()

        elif event == "AF_S":
            self._af.do_support()

        elif event == "AF_E":
            self._af.do_extraction()

        elif event == "AF_I":
            self._af.do_interception()

        elif event == "N_G":
            self._navy.do_gunfire()

        elif event == "N_E":
            self._navy.do_extraction()

        elif event == "N_I":
            self._navy.do_interception()
