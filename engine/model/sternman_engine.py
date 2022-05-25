from engine.engine import Engine
from utils.validators import validate_integer, validate_boolean


class SternmanEngine(Engine):

    def __init__(self, last_service_mileage: int, warning_light_is_on: bool):
        """
        Args:
            last_service_mileage (int): Mileage tracked during last service.
            warning_light_is_on (bool): Warning light is on or not.
        """
        super().__init__()

        validate_integer('last_service_mileage', last_service_mileage, 0)
        self._last_service_mileage = last_service_mileage

        validate_boolean('warning_light_is_on', warning_light_is_on)
        self._warning_light_is_on = warning_light_is_on

    def need_service(self) -> bool:
        """
        Whether the engine needs servicing.

        Returns:
            bool 
        """
        return self._warning_light_is_on
