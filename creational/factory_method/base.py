from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    """
    The Factory base class.
    Declares the factory_method method that is supposed to return an object of a Phone class.
    The Factory's subclasses usually provide the implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Abstract method for returning the phone a Factory will retrieve.
        """
        raise NotImplementedError

    def do_business_operation(self) -> str:
        """
        Method for executing some operation.

        :return: The phone.
        """

        phone = self.factory_method()
        return f"Factory: Retrieving phone: {phone.get_phone()}"


class Phone(metaclass=ABCMeta):
    """
    The Phone interface.
    Declares the get_phone method that returns the phone.
    """

    @abstractmethod
    def get_phone(self) -> str:
        raise NotImplementedError
