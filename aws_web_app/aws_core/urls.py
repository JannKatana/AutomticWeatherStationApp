from django.urls import path
from aws_core import views

# TEMPLATE TAGGING
app_name = 'aws_core'


urlpatterns = [
	path('station/add/', views.station_add, name='add_station'),
	path('stations/', views.station_list, name='station_list'),
]