from engine.engine import Engine
from utils.validators import validate_integer, validate_boolean


class SternmanEngine(Engine):

    def __init__(self, warning_light_is_on: bool):
        """
        Args:
            warning_light_is_on (bool): Warning light is on or not
        """
        super().__init__()

        validate_boolean('warning_light_is_on', warning_light_is_on)
        self._warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """
        Whether the engine needs servicing

        Returns:
            bool 
        """
        return self._warning_light_is_on
