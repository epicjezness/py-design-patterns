from .base import SpaceTransformer


class HyphenSpaceTransformer(SpaceTransformer):
    """
    Class for transforming spaces in a given string into hyphens.
    """

    def transform(self, req: str) -> str:
        """
        Method for transforming spaces in strings into hyphens.

        :param req: The string to transform.
        """

        return '-'.join(req.split())


class UnderscoreTransformer(object):
    """
    Class for transforming spaces in a fiven string into underscores.
    Does not follow the SpaceTransformer interface.
    """

    @staticmethod
    def convert_to_hyphen(req: str) -> str:
        """
        Method for transforming spaces in strings into underscores.

        :param req: The string to transform.
        """

        return '_'.join(req.split())
