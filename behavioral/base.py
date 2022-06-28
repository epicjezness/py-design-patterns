from abc import ABCMeta, abstractmethod


class BehavioralDemoService(metaclass=ABCMeta):
    """
    The BehavioralDemoService interface.
    Declares a method used for executing the demo routine.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method for executing the demo routine.
        """

        raise NotImplementedError
