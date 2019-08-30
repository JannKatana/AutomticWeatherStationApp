from django import forms
from aws_core.models import StationType, StationDataField

class StationForm(forms.Form):
	station_name = forms.CharField()
	station_type = forms.ModelChoiceField(queryset=StationType.objects.all())
	station_num  = forms.CharField()
	location_lat = forms.FloatField()
	loaction_lon = forms.FloatField()
	column_names = forms.ModelMultipleChoiceField(queryset=StationDataField.objects.all())
