import logging
from abc import ABC, abstractmethod

LOGGER = logging.getLogger(__name__)


class SpaceTransformer(ABC):
    """
    Base class for SpaceTransformer objects.
    Transform spaces in a given string into another character.
    """

    @abstractmethod
    def transform(self, req: str) -> str:
        """
        Abstract method for transforming spaces in strings.

        :param req: The string to transform.
        """

        raise NotImplementedError
