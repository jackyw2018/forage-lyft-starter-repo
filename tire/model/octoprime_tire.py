from tire.tire import Tire
from ..utils.validators import validate_list_of_floats


class OctoprimeTire(Tire):

    _TOTAL_WEARNESS_TO_SERVICE = 3
    _TIRE_COUNT = 4

    def __init__(self, tires_wearness):
        """
        Args:
            tires_wearness (list(float)): Tires wearness
        """
        super().__init__()

        validate_list_of_floats('tires_wearness', tires_wearness,
                                OctoprimeTire._TIRE_COUNT, min_value_each=0, max_value_each=1)
        self._tire_wearness = tires_wearness

    def needs_service(self) -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool
        """
        return sum(self._tire_wearness) >= OctoprimeTire._TOTAL_WEARNESS_TO_SERVICE
