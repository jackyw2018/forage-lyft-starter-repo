from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def need_service() -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool 
        """
        pass

    @staticmethod
    def mileage_travelled(starting_mileage: int, ending_mileage: int) -> int:

        return ending_mileage - starting_mileage
