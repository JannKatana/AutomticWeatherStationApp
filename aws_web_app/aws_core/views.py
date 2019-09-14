from django.http import HttpResponse
from django.shortcuts import render
from aws_core import forms
from aws_core.models import StationType, Station, StationData, StationDataField

import json
# Create your views here.

def index(request):
	if request.method == 'POST' and request.is_ajax():
		pk = request.POST.get('pk')
		pinned = request.POST.get('pinned')
		station = Station.objects.get(id=pk)

		field_names = station.column_names.all()
		data_to_show = StationData.objects.filter(station=station).order_by('-id')

		if len(data_to_show) != 0:
			data_to_show = data_to_show[0].data.split('#')

		response = {}
		for field_name, data in zip(field_names, data_to_show):
			response[field_name.name] = data
		return HttpResponse(json.dumps(response), content_type="application/json")

	pinned_stations = Station.objects.filter(pinned=True)
	return render(request, 'aws_core/index.html', {'pinned_stations':pinned_stations})


def station_add(request):
	form = forms.StationForm()

	if request.method == 'POST':
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
	if request.method == 'POST':
		pk = request.POST.get('pk')
		pinned = request.POST.get('pinned')
		station = Station.objects.get(id=pk)

		if (pinned == 'true'):
			station.pinned = True
		else:
			station.pinned = False

		station.save()

	station_list = Station.objects.all().order_by('station_name')
	
	data_list = []
	for station in station_list:
		field_names = station.column_names.all()
		data_to_show = StationData.objects.filter(station=station).order_by('-id')

		if len(data_to_show) != 0:
			data_to_show = data_to_show[0].data.split('#')

		data = [station, zip(field_names, data_to_show)]
		data_list.append(data)

	return render(request, 'aws_core/station_list.html', {'data_list':data_list})
