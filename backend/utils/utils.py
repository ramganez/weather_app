# utility funcaitons

import re

from datetime import datetime


def clean_date_time_local(data):
    """
    clean date field, to support Django's DATE_INPUT_FORMATS.
    ref - https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATE_INPUT_FORMATS

    data: "2022-10-10 02:00:00 CDT"

    return : "2022-10-10 02:00:00"
    """
    return datetime.strptime(re.sub("[^0-9-: ]", "", data), "%Y-%m-%d %H:%M:%S ")

def separate_date_time(data_list):
    """
    separate date time before sending to frontend.

    data: "data dict"

    return : "data dict with date & time formatted"
    """
    for data in data_list:
        data['date'] = datetime.strftime(data['date_time_local'], "%a %d")
        data['time'] = datetime.strftime(data['date_time_local'], "%H:%M")
    return data_list