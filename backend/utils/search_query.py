from unittest import result
from django.db.models import Q
from datetime import timedelta
import datetime

from app.models import WeatherData


def select_days(query):
    """
    Select next 7 days of data
    Args:
        query: search date
    Returns:
        return WeatherData object results
    Raises:
    """

    given_date = datetime.datetime.strptime(query, "%Y-%m-%d")  #'2022-10-07 15:00'
    day_7 = given_date + timedelta(days=6)
    results = WeatherData.objects.filter(
        Q(date_time_local__lte=day_7) & Q(date_time_local__gte=given_date)
    )
    return results


def select_days_with_time(query):
    """
    Select next 7 days of data and select specific time
    Args:
        query: search date
    Returns:
        return WeatherData object results
    Raises:
    """

    given_date = datetime.datetime.strptime(
        query, "%Y-%m-%d %H:%M"
    )  #'2022-10-07 15:00'
    day_7 = given_date + timedelta(days=6)
    results = WeatherData.objects.filter(
        Q(date_time_local__lte=day_7)
        & Q(date_time_local__gte=given_date)
        & Q(date_time_local__hour=given_date.hour)
    )
    return results
