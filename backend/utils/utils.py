# utility funcaitons

import re


def clean_date_time_local(data):
    """
    clean date field, to support Django's DATE_INPUT_FORMATS.
    ref - https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATE_INPUT_FORMATS

    data: "2022-10-10 02:00:00 CDT"

    return : "2022-10-10 02:00:00"
    """
    return re.sub("[^0-9-: ]", "", data)
