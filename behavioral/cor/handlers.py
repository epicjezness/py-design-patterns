import logging
from typing import Any

from .base import BaseHandler

LOGGER = logging.getLogger(__name__)


class JSONHandler(BaseHandler):
    def handle(self, request: str) -> str:
        """
        Method for handling a request.

        :param request: The request object.
        """

        if request == "JSON":
            return f"JSONHandler: Handled the JSON."

        else:
            LOGGER.info('JSONHandler: Unable to handle request. Passing to next handler.')
            return super().handle(request)


class XMLHandler(BaseHandler):
    def handle(self, request: Any) -> str:
        """
        Method for handling a request.

        :param request: The request object.
        """

        if request == "XML":
            return f"XMLHandler: Handled the XML."

        else:
            LOGGER.info('XMLHandler: Unable to handle request. Passing to next handler.')
            return super().handle(request)


class YAMLHandler(BaseHandler):
    def handle(self, request: str) -> str:
        """
        Method for handling a request.

        :param request: The request object.
        """

        if request == "YAML":
            return f"YAMLHandler: Handled the YAML."

        else:
            LOGGER.info('YAMLHandler: Unable to handle request. Passing to next handler.')
            return super().handle(request)
