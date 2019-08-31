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
		try:
			station_type = StationType.objects.get(id=request.POST.get('station_type'))
		except ValueError:
			station_type = StationType.objects.create(type_name=request.POST.get('station_type'))

		column_names = request.POST.getlist('column_names')
		station = Station.objects.create(
			station_name = request.POST.get('station_name'),
			station_num  = request.POST.get('station_num'),
			station_type = station_type,
			location_lat = request.POST.get('location_lat'),
			location_lon = request.POST.get('location_lon'),
		)

		for column_id in column_names:
			try:
				field_name = StationDataField.objects.get(id=column_id)
			except ValueError:	
				field_name = StationDataField.objects.create(name=column_id)

			station.column_names.add(field_name)


	return render(request, 'aws_core/new_station_page.html', {'form':form})

def station_list(request):
	station_list = Station.objects.all().order_by('station_name')
	return render(request, 'aws_core/station_list.html', {'stations':station_list})
