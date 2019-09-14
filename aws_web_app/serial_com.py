import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','aws_web_app.settings')

import django
django.setup()

from aws_core.models import StationData

import serial
import time
import re


if __name__ == '__main__':
    serial_config = open("settings.config", "r")
    port = serial_config.read()

    print("Starting communication at ", port, "...")
    com_port = serial.Serial(port, 19200, timeout=3)
    # com_port.write(b"AT+CMGF=1\r")
    # time.sleep(1)
    # com_port.write(b"AT+CNMI=2,2,0,0,0\r")
    # time.sleep(1)    
    # com_port.flushInput()
    phone_num = ""
    while True:
        try:
            ser_bytes = com_port.readline()
            msg = str(ser_bytes)
            if len(ser_bytes) > 0:
                x = re.search("CMT", msg)
                if x:
                    phone_num_list = re.findall('[0-9]{12}', msg)
                    phone_num = "+" + phone_num_list[0]
                else:
                    data = re.findall("[0-9]+", msg)
                    if len(data) > 0:
                        # save to database
                        # save_to_db(phone_num, data)
                        print(data)
                        print("record has been saved.")

        except Exception as e:
            print(e)
            print("Unexpected error occured. /!\\ (>_<) /!\\")
            break