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
# process : 抽水 10秒 -> 停 10分鐘 -> 拍照上傳

class Rpi_photo:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def pump(self, pin, t1):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # set pin
        pump_pin = pin
        print(pump_pin)
        GPIO.setup(pump_pin, GPIO.OUT, initial = GPIO.LOW)

        # step 1, 抽水 10sec
        GPIO.output(pump_pin, GPIO.HIGH) # Turn on
        time.sleep(t1)
        print(t1)
        GPIO.output(pump_pin, GPIO.LOW) # Turn off

    def up_photo(self, devid):
        #os.system("python3 stepmotor.py --rotate %s" %rotate_number2)
        #arch = subprocess.check_output("python3 print.py", shell=True);
        #print(arch)
        #os.system("docker run --rm -d --device /dev/camera1:/dev/camera1 -v /home/pi/capture-workspace:/tmp/capture-workspace -e \"TZ=Asia/Taipei\" --name capture jadezzz/capture-tools:latest")
        #print("1")
        os.system("docker exec capture python3 capture.py -c /dev/camera1 -s \"1600x1200\"")
        print("2")
        os.system(devid)
        #os.system("docker exec capture python3 upload.py -u \"http://140.116.246.178:8888/upload/picture/fish-algae/[deviceid]\" -m \"picture\"")
        # request count
        #crontab
        print("3")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-id", "--devid", type = int, default = 1,  help="device id")
    args = vars(ap.parse_args())
    
    upload_path = "docker exec capture python3 upload.py -u \"http://140.116.246.178:8888/upload/picture/fish-algae/"+str(args['devid'])+"\" -m \"picture\""
    
    s = Rpi_photo(1,2)
    s.pump(20,2)
    time.sleep(5)
    s.up_photo(upload_path)
    time.sleep(10)
    r = requests.get("http://140.116.246.178:8888/fish-algae/1/latest-count")
    res=r.json()
    value = res['count']
    print(res, value)
    #button_gpio = 16
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(button_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #pressed = False
    '''
    while True:
        if not GPIO.input(button_gpio):
            if not pressed:
                print("button pressed")
                pressed = True
                s.pump(8,10)
                time.sleep(6)
                s.up_photo(upload_path)
                time.sleep(10)
                r = requests.get("http://140.116.246.178:8888/fish-algae/1/latest-count")
                res=r.json()
                value = res['count']
                print(res, value)
            else:
                pressed = False
            time.sleep(0.1)
       '''     


