from django.contrib import admin
from aws_core.models import StationType, StationData, Station, StationDataField

# Register your models here.
admin.site.register(StationType)
admin.site.register(StationData)
admin.site.register(Station)
admin.site.register(StationDataField)