from abc import ABC, abstractmethod


class StructuralDemoService(ABC):
    """
    The StructuralDemoService interface.
    Declares a method used for executing the demo routine.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method for executing the demo routine.
        """

        raise NotImplementedError
