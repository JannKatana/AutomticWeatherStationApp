from django.shortcuts import render
from django.http import HttpResponse
from aws_core.models import StationType, Station, StationData
from aws_core import forms

# Create your views here.

def index(request):
	return render(request, 'aws_core/index.html')


def new_station_view(request):
	form = forms.StationForm()

	if request.method == 'POST':
		form = forms.StationForm(request.POST)
		if form.is_valid():
			print('Station Name: ', form.cleaned_data['station_name'])
			print('Station Num: ', form.cleaned_data['station_num'])

	return render(request, 'aws_core/new_station_page.html', {'form':form})