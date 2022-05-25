from engine.engine import Engine
from utils.validators import validate_integer


class CapuletEngine(Engine):

    _MILEAGE_TO_SERVICE = 30_000

    def __init__(self, last_service_mileage: int, current_mileage: int):
        """
        Args:
            last_service_mileage (int): Mileage tracked during last service
            current_mileage (int): Mileage traveled thus far
        """
        super().__init__()

        validate_integer('last_service_mileage', last_service_mileage, 0)
        self._last_service_mileage = last_service_mileage

        validate_integer('current_mileage', current_mileage,
                         last_service_mileage, custom_min_message='Current mileage should be greater than last service mileage.')
        self._current_mileage = current_mileage

    def needs_service(self) -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool 
        """
        return self.mileage_since_last_service >= CapuletEngine._MILEAGE_TO_SERVICE

    @property
    def mileage_since_last_service(self) -> int:
        """
        Mileage since last servicing

        Returns:
            int: 
        """
        return self._current_mileage - self._last_service_mileage
