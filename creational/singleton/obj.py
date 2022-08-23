from .base import SingletonMeta


class SingletonObject(metaclass=SingletonMeta):
    """
    Class implementing SingletonMeta as its metaclass.
    """

    def do_something(self):
        """
        Method for doing something.
        """

        pass
