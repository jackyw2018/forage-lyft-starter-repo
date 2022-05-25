from tire.tire import Tire
from ..utils.validators import validate_list_of_floats


class CarriganTire(Tire):

    _WEARNESS_TO_SERVICE = 0.9
    _TIRE_COUNT = 4

    def __init__(self, tires_wearness):
        """
        Args:
            tires_wearness (list(float)): Tires wearness
        """
        super().__init__()

        validate_list_of_floats('tires_wearness', tires_wearness,
                                CarriganTire._TIRE_COUNT, min_value_each=0, max_value_each=1)
        self._tire_wearness = tires_wearness

    def needs_service(self) -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool
        """
        for w in self._tire_wearness:
            if w >= CarriganTire._WEARNESS_TO_SERVICE:
                return True

        return False
