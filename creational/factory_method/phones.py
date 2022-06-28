from .base import Phone


class IPhonePhone(Phone):
    """
    Concrete Phone class implementation for iPhone.
    """

    def get_phone(self) -> str:
        return "Here is your Apple iPhone."


class GalaxyS22Phone(Phone):
    """
    Concrete Phone class implementation for Galaxy S22.
    """

    def get_phone(self) -> str:
        return "Here is your Samsung Galaxy S22."
