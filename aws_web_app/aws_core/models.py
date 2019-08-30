from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Incorrect format. Please try again.")

class StationType(models.Model):
    type_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.type_name


class Station(models.Model):
    station_name = models.CharField(max_length=64, unique=True)
    station_type = models.OneToOneField(StationType, on_delete=models.CASCADE)
    station_num  = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    location_lat = models.FloatField()
    loaction_lon = models.FloatField()
    column_names = models.CharField(max_length=256)

    def __str__(self):
        return self.station_name


class StationData(models.Model):
    data_row     = models.CharField(max_length=256)
    station      = models.ForeignKey(Station, on_delete=models.CASCADE)
