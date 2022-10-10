from django.forms import ModelForm, ClearableFileInput
from app.models import WeatherDataFile

# Create the form class.
class WeatherDataForm(ModelForm):
    class Meta:
        model = WeatherDataFile
        fields = ["data_file"]
        widgets = {
            'data_file': ClearableFileInput(attrs={'class': 'form-control form-control-lg'}),
        }
