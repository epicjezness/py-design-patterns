from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface.
    Declares a method for building the chain of handlers and another method for handling a request.
    """

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        """
        Abstract method for setting the next handler.

        :param handler: The Handler object.
        """

        raise NotImplementedError

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        """
        Abstract method for handling a request.

        :param request: The request object.
        """

        raise NotImplementedError


class BaseHandler(Handler):
    """
    Base class for Handler objects.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        """
       Method for setting the next handler.

       :param handler: The Handler object.
       """

        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        """
        Method for handling a request.

        :param request: The request object.
        """

        if self._next_handler:
            return self._next_handler.handle(request)
