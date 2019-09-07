from django.http import HttpResponse
from django.shortcuts import render
from aws_core import forms
from aws_core.models import StationType, Station, StationData, StationDataField

# Create your views here.

def index(request):
	return render(request, 'aws_core/index.html')


def station_add(request):
	form = forms.StationForm()

	if request.method == 'POST':
		print(request.POST)
		try:
			station_type = StationType.objects.get(id=request.POST.get('station_type'))
		except ValueError:
			station_type = StationType.objects.create(type_name=request.POST.get('station_type'))

		station = Station.objects.create(
			station_name = request.POST.get('station_name'),
			station_num  = request.POST.get('station_num'),
			station_type = station_type,
			location_lat = request.POST.get('location_lat'),
			location_lon = request.POST.get('location_lon'),
		)

		column_names = request.POST.get('data_columns')
		column_names = column_names[:-1]
		column_names = column_names.split("#")

		for column_name in column_names:
			field_name = StationDataField.objects.get_or_create(name=column_name)[0]
			station.column_names.add(field_name)


	return render(request, 'aws_core/new_station_page.html', {'form':form})

def station_list(request):
	station_list = Station.objects.all().order_by('station_name')
	return render(request, 'aws_core/station_list.html', {'stations':station_list})
