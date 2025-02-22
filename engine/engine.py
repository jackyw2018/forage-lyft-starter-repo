from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service() -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool 
        """
        pass
