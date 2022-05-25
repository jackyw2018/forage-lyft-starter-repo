from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service() -> bool:
        """
        Whether the tire needs serivcing

        Returns:
            bool 
        """
        pass
