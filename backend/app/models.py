from weakref import WeakMethod
from django.db import models
from traitlets import default

from utils.utils import clean_date_time_local
from config import DATA_TYPE, COLUMN_NAMES

# Create your models here.


class WeatherDataFile(models.Model):
    # file will be uploaded to app/uploads
    data_file = models.FileField(upload_to="uploads/")
    data_type = models.CharField(max_length=2, choices = DATA_TYPE)

class WeatherData(models.Model):
    """
    Save all the WeatherData from uploaded files.
    Fields are set from config variable.
    """
    class Meta:
        ordering = ['date_time_local']

    def save(self, *args, **kwargs):
        # clean date time field before insert
        self.date_time_local = self.date_time_local and  clean_date_time_local(self.date_time_local)
        super(WeatherData, self).save(*args, **kwargs)    

for field in COLUMN_NAMES:
    if field in ['date_time_local', 'date']:
        WeatherData.add_to_class(field, models.DateTimeField(null=True))
    else:
        WeatherData.add_to_class(field, models.CharField(max_length=100))
WeatherData.add_to_class("data_file", models.ForeignKey(WeatherDataFile, on_delete=models.CASCADE))
