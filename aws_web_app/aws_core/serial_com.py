import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','aws_web_app.settings')

import django
django.setup()

from aws_core.models import StationData