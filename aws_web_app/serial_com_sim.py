import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','aws_web_app.settings')

import django
django.setup()

from aws_core.models import StationData, Station

if __name__ == '__main__':
	while True:

		print("Enter a phone number:")
		phone_num = input()
		if phone_num == 'q':
			break;

		print("Enter Data:")
		data = input()
		if data == 'q':
			break;

		print("Saving record...")

		station = Station.objects.get(station_num=phone_num)
		station_data = StationData.objects.create(station=station,data=data)

		print("record saved")

	print("Closing app...")
