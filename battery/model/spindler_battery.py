from battery.battery import Battery
from ..utils.validators import validate_date
from ..utils.datetime_helpers import DAYS_IN_YEAR

from datetime import datetime, timedelta


class SpindlerBattery(Battery):

    _SERVICE_THRESHOLD_YEAR = 2
    _SERVICE_THRESHOLD_TIMEDELTA = timedelta(
        days=_SERVICE_THRESHOLD_YEAR*DAYS_IN_YEAR)

    def __init__(self, last_service_date: datetime.date, current_date: datetime.date):
        """
        Args:
            last_service_date (date): The date of last service
            current_date (date): Current date
        """
        super().__init__()

        validate_date('last_service_date', last_service_date,
                      max_value=datetime.today().date())
        self._last_service_date = last_service_date

        validate_date('current_date', current_date,
                      min_value=last_service_date)
        self._current_date = current_date

    def needs_service(self) -> bool:
        """
        Whether the battery needs serivcing

        Returns:
            bool
        """
        return self.days_since_last_service > SpindlerBattery._SERVICE_THRESHOLD_TIMEDELTA

    @property
    def days_since_last_service(self) -> timedelta:
        """
        Days since last servicing

        Returns:
            timedelta:
        """
        return self._current_date - self._last_service_date
