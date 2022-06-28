from abc import ABCMeta, abstractmethod


class CreationalDemoService(metaclass=ABCMeta):
    """
    The CreationalDemoService interface.
    Declares a method used for executing the demo routine.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method for executing the demo routine.
        """

        raise NotImplementedError
