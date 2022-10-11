COLUMN_NAMES_HOURLY = ["date_time_local", "wind_dir", "wind_speed", "relative_humidity", "temperature"]

COLUMN_NAMES_DAILY = [
    "date",
    "max_temperature",
    "min_temperature",
    "avg_relative_humidity",
    "avg_wind_speed",
    "sunrise",
    "sunset",
]

COLUMN_NAMES = COLUMN_NAMES_HOURLY + COLUMN_NAMES_DAILY 

DATA_TYPE = (
    (1, 'HOURLY'),
    (2, 'DAY'),
    (10, 'MIXED')
)