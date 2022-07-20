from .base import SpaceTransformer
from .transformers import UnderscoreTransformer


class UnderscoreToHyphenAdapter(SpaceTransformer, UnderscoreTransformer):
    """
    Adapter class for UnderscoreTransformer to implement the same function as SpaceTransformer objects.
    """

    def transform(self, req: str) -> str:
        """
        Method for transforming underscores in strings into hyphens.

        :param req: The string to transform.
        """

        init = self.convert_to_hyphen(req)
        return "-".join(init.split("_"))
