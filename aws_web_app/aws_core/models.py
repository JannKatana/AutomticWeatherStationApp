from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Incorrect format. Please try again.")

class StationType(models.Model):
    type_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.type_name


class StationDataField(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name 


class Station(models.Model):
    station_name = models.CharField(max_length=64, unique=True)
    station_type = models.ForeignKey(StationType, on_delete=models.CASCADE)
    station_num  = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    location_lat = models.FloatField(blank=True, null=True)
    location_lon = models.FloatField(blank=True, null=True)
    column_names = models.ManyToManyField(StationDataField)
    pinned       = models.BooleanField(default=False)

    def __str__(self):
        return self.station_name


class StationData(models.Model):
    station    = models.ForeignKey(Station, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)
    data       = models.CharField(max_length=256)

