import sys
import argparse
import logging
from logging import critical, error, info, warning, debug
import RPi.GPIO as GPIO
#import RPistepper as stp
import time
import os
import subprocess
from gpiozero import Button
import requests
import json
from pyModbusTCP.client import ModbusClient
# process : 抽水 10秒 -> 停 10分鐘 -> 拍照上傳

class Rpi_photo:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def pump(self, pin, t1, t2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # set pin
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)

        # step 1, 抽水 10sec
        GPIO.output(pin, GPIO.HIGH) # Turn on
        time.sleep(t1)
        GPIO.output(pin, GPIO.LOW) # Turn off
        time.sleep(t2)

    def up_photo(self, devid):
        #os.system("python3 stepmotor.py --rotate %s" %rotate_number2)
        #arch = subprocess.check_output("python3 print.py", shell=True);
        #print(arch)
        #os.system("docker run --rm -d --device /dev/camera1:/dev/camera1 -v /home/pi/capture-workspace:/tmp/capture-workspace -e \"TZ=Asia/Taipei\" --name capture jadezzz/capture-tools:latest")
        #print("1")
        os.system("docker exec capture python3 capture.py -c /dev/camera1 -s \"1600x1200\"")
        os.system(devid)
        #os.system("docker exec capture python3 upload.py -u \"http://140.116.246.178:8888/upload/picture/fish-algae/1\" -m \"picture\"")
    
    def modb(self, value):
        connected = False
        while connected == False:
            try:
                c = ModbusClient(host="192.168.250.12", port=502, auto_open=True, unit_id=1, debug=True) #auto_open for keep TCP open.
                print("Connected to PLC")
                connected = True
            except ValueError:
                print("Error with host or port params")
                connected = False
        written = c.write_single_register(101, value)
        while not written:
            written = c.write_single_register(101, value)
            print("writing value to PLC")

if __name__ == "__main__":
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-id", "--devid", type = int, default = 1,  help="device id")
    #args = vars(ap.parse_args())
    time1 = None
    time2 = None
    deviceid = None
    with open('/home/pi/Desktop/Raspberry-Pi-master/data.json') as js:
        dic = json.load(js)
        time1 = dic['time1']
        time2 = dic['time2']
        deviceid = dic['deviceid']
    print("Device id: "+str(deviceid))
    print("Pump time: "+str(time1))
    print("Wait time: "+str(time2))
    upload_path = "docker exec capture python3 upload.py -u \"http://140.116.246.178:8888/upload/picture/fish-algae/"+str(deviceid)+"\" -m \"picture\""
    
    s = Rpi_photo(1,2)
    s.pump(20, time1, time2)
    s.up_photo(upload_path)
    time.sleep(10)
    r = requests.get("http://140.116.246.178:8888/fish-algae/1/latest-count")
    res=r.json()
    value = res['count']
    print("Number of algae: ", str(value))
    #s.modb(value)
    

