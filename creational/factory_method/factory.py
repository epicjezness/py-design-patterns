from .base import Factory, Phone
from .phones import GalaxyS22Phone, IPhonePhone


class IPhoneFactory(Factory):
    """
    Concrete Factory implementation for iPhone phones.
    """

    def factory_method(self) -> Phone:
        return IPhonePhone()


class GalaxyS22Factory(Factory):
    """
    Concrete Factory implementation for GalaxyS22 phones.
    """

    def factory_method(self) -> Phone:
        return GalaxyS22Phone()
