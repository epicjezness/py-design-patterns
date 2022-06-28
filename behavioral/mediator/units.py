import logging

from .base import Component

LOGGER = logging.getLogger(__name__)


class Army(Component):
    """
    Concrete Component class used for demonstrating the Mediator object it belongs to.
    """

    # Call
    def call_naval_gunfire(self) -> None:
        LOGGER.info(f"Requesting naval gunfire! Over.")
        self.mediator.notify(self, 'N_G')

    def call_naval_extraction(self) -> None:
        LOGGER.info(f"Requesting naval extraction! Over.")
        self.mediator.notify(self, 'N_E')

    def call_naval_interception(self) -> None:
        LOGGER.info(f"Requesting naval interception! Over.")
        self.mediator.notify(self, 'N_I')

    def call_air_support(self) -> None:
        LOGGER.info(f"Requesting air support! Over.")
        self.mediator.notify(self, 'AF_S')

    def call_air_extraction(self) -> None:
        LOGGER.info(f"Requesting air extraction! Over.")
        self.mediator.notify(self, 'AF_E')

    def call_air_interception(self) -> None:
        LOGGER.info(f"Requesting aerial interception! Over.")
        self.mediator.notify(self, 'AF_I')

    # Do
    def do_interception(self) -> None:
        LOGGER.info(f"Copy. Ground units intercepting.")
        self.mediator.notify(self, 'END')


class Navy(Component):
    """
    Concrete Component class used for demonstrating the Mediator object it belongs to.
    """

    # Call
    def call_air_support(self) -> None:
        LOGGER.info(f"Requesting air support! Over.")
        self.mediator.notify(self, 'AF_S')

    def call_air_interception(self) -> None:
        LOGGER.info(f"Requesting aerial interception! Over.")
        self.mediator.notify(self, 'AF_I')

    def call_ground_interception(self) -> None:
        LOGGER.info(f"Requesting ground interception! Over.")
        self.mediator.notify(self, 'G_I')

    # Do
    def do_gunfire(self) -> None:
        LOGGER.info(f"Copy. Naval gunfire inbound.")
        self.mediator.notify(self, 'END')

    def do_extraction(self) -> None:
        LOGGER.info(f"Copy. Naval extraction inbound.")
        self.mediator.notify(self, 'END')

    def do_interception(self) -> None:
        LOGGER.info(f"Copy. Amphibious units intercepting.")
        self.mediator.notify(self, 'END')


class AirForce(Component):
    """
    Concrete Component class used for demonstrating the Mediator object it belongs to.
    """

    # Call
    def call_naval_gunfire(self) -> None:
        LOGGER.info(f"Requesting naval gunfire! Over.")
        self.mediator.notify(self, 'N_G')

    def call_naval_interception(self) -> None:
        LOGGER.info(f"Requesting naval interception! Over.")
        self.mediator.notify(self, 'N_I')

    def call_ground_interception(self) -> None:
        LOGGER.info(f"Requesting ground interception! Over.")
        self.mediator.notify(self, 'G_I')

    # Do
    def do_support(self) -> None:
        LOGGER.info(f"Copy. Air support inbound.")
        self.mediator.notify(self, 'END')

    def do_extraction(self) -> None:
        LOGGER.info(f"Copy. Air extraction inbound.")
        self.mediator.notify(self, 'END')

    def do_interception(self) -> None:
        LOGGER.info(f"Copy. Airborne units intercepting.")
        self.mediator.notify(self, 'END')
