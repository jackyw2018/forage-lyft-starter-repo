from abc import ABC, abstractmethod


class Battery(ABC):
    @ abstractmethod
    def needs_service() -> bool:
        """
        Whether the battery needs serivcing

        Returns:
            bool
        """
        pass
