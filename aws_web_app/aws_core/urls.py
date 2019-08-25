from django.urls import path
from aws_core import views

urlpatterns = [
	path('', views.index, name='index'),
]