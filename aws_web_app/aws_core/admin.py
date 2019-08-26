from django.contrib import admin
from aws_core.models import Station_Type, Station_Data, Station

# Register your models here.
admin.site.register(Station_Type)
admin.site.register(Station_Data)
admin.site.register(Station)