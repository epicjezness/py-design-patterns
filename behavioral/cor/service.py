import logging

from .handlers import JSONHandler, XMLHandler, YAMLHandler
from ..base import BehavioralDemoService

LOGGER = logging.getLogger(__name__)


class CORBehavioralDemoService(BehavioralDemoService):
    """
    Class for demonstrating the mediator pattern.
    """

    _json_handler: JSONHandler = None
    _xml_handler: XMLHandler = None
    _yaml_handler: YAMLHandler = None

    def _create_handlers(self) -> None:
        """
        Private method for creating handler objects and setting the handler chain.
        """

        LOGGER.info('Creating mediator and its components...')
        self._json_handler = JSONHandler()
        self._xml_handler = XMLHandler()
        self._yaml_handler = YAMLHandler()

        self._json_handler.set_next(self._xml_handler).set_next(self._yaml_handler)

    def _do_handling(self) -> None:
        """
        Private method for executing the handler chain.
        """

        requests = ['JSON', 'XML', 'YAML', 'PNG']
        LOGGER.info(f'Processing requests: {requests}')

        for req in requests:
            LOGGER.info(f"Processing request: {req}")
            result = self._json_handler.handle(req)

            if result:
                LOGGER.info(result)

            else:
                LOGGER.info(f"{req} was left unprocessed.")

    def execute(self) -> None:
        """
        Method for executing the demo routine of the mediator pattern.
          - Creates the handlers and set the handler chain.
          - Do component calls through the mediator.
        """

        LOGGER.info('Executing demo routine...')
        self._create_handlers()
        self._do_handling()
        LOGGER.info('Demo routine Finished.')
