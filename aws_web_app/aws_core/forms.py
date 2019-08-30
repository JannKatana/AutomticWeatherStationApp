from django import forms

class StationForm(forms.Form):
	station_name = forms.CharField()
	# station_type = forms.OneToOneField(StationType, on_delete=models.CASCADE)
	station_num  = forms.CharField()
	location_lat = forms.FloatField()
	loaction_lon = forms.FloatField()
	column_names = forms.CharField(widget=forms.Textarea)
