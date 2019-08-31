from django import forms
from django.core import validators
from aws_core.models import StationType, StationDataField, Station
from django_select2.forms import Select2MultipleWidget, Select2Widget, Select2TagWidget

class StationForm(forms.ModelForm):

	station_name = forms.CharField(
		label='Station Name',
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)

	station_type = forms.ModelChoiceField(
		label='Type', 
		queryset=StationType.objects.all(),
		widget=Select2TagWidget(attrs={'class': 'form-control'}),
	)

	station_num  = forms.CharField(
		label='Cell Number', 
		widget=forms.TextInput(attrs={'class': 'form-control'}),		
	)

	location_lat = forms.FloatField(
		label='Latitude',
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)

	location_lon = forms.FloatField(
		label='Longitude',
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)

	column_names = forms.ModelMultipleChoiceField(
		label='Data Columns',
		queryset=StationDataField.objects.all(),
		widget=Select2TagWidget(attrs={'class': 'form-control'}),
	)

	class Meta():
		model = Station
		fields = '__all__'

