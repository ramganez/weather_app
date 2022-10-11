import csv
import config

from app.models import WeatherData


def save_forecast_details(form_obj):
    """
    Save daily forecast from CSV to Data model
    Args:
        file_path: path of the file
    Returns:
        return None
    Raises:
    """

    with open(form_obj.data_file.path, "r") as fp:
        forecast_details = csv.DictReader(fp, delimiter=",")
        if (
            config.COLUMN_NAMES_HOURLY[0] in forecast_details.fieldnames
            and config.COLUMN_NAMES_DAILY[0] in forecast_details.fieldnames
        ):
            form_obj.data_type = 10  # MIXED
        if config.COLUMN_NAMES_HOURLY[0] in forecast_details.fieldnames:
            form_obj.data_type = 1  # HOURLY
        if config.COLUMN_NAMES_DAILY[0] in forecast_details.fieldnames:
            form_obj.data_type = 2  # DAILY

        for forecast in forecast_details:
            
            WeatherData.objects.create(
                **{k: v for k, v in forecast.items() if k in config.COLUMN_NAMES}
            )

        fp.close()
