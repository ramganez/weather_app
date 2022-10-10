from django.db import models

# Create your models here.


class WeatherDataFile(models.Model):
    # file will be uploaded to app/uploads
    data_file = models.FileField(upload_to="uploads/")
