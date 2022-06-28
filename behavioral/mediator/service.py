import logging

from .relay import CommunicationsRelay
from .units import AirForce, Army, Navy
from ..base import BehavioralDemoService

LOGGER = logging.getLogger(__name__)


class MediatorBehavioralDemoService(BehavioralDemoService):
    """
    Class for demonstrating the mediator pattern.
    """

    _af: AirForce = None
    _army: Army = None
    _navy: Navy = None
    _mediator: CommunicationsRelay = None

    def _create_mediator_and_components(self) -> None:
        """
        Private method for creating components with the same Mediator object.
        """

        LOGGER.info('Creating mediator and its components...')
        self._af = AirForce()
        self._army = Army()
        self._navy = Navy()

        self._mediator = CommunicationsRelay(self._army, af=self._af, navy=self._navy)

    def _do_component_calls(self) -> None:
        LOGGER.info('Executing AirForce to Navy coms...')
        self._af.call_naval_gunfire()
        self._af.call_naval_interception()

        LOGGER.info('Executing AirForce to Army coms...')
        self._af.call_ground_interception()

        LOGGER.info('Executing Navy to AirForce coms...')
        self._navy.call_air_support()
        self._navy.call_air_interception()

        LOGGER.info('Executing Navy to Army coms...')
        self._navy.call_ground_interception()

        LOGGER.info('Executing Army to AirForce coms...')
        self._army.call_air_support()
        self._army.call_air_extraction()
        self._army.call_air_interception()

        LOGGER.info('Executing AirForce to Navy coms...')
        self._army.call_naval_gunfire()
        self._army.call_naval_extraction()
        self._army.call_naval_interception()

    def execute(self) -> None:
        """
        Method for executing the demo routine of the mediator pattern.
          - Creates the mediator and its components.
          - Do component calls through the mediator.
        """

        LOGGER.info('Executing demo routine...')
        self._create_mediator_and_components()
        self._do_component_calls()
        LOGGER.info('Demo routine Finished.')
