import sys
import argparse
import logging
from logging import critical, error, info, warning, debug
#import RPi.GPIO as GPIO
#import RPistepper as stp
import time
import os
import subprocess

# process : 抽水 10秒 -> 停 10分鐘 -> 拍照上傳

class Rpi_photo:
	def __init__(self, time1, time2):
		self.time1 = time1
		self.time2 = time2

	def pump(self, pin, t1):
		#GPIO.setmode(GPIO.BCM)
		#GPIO.setwarnings(False)

		# set pin
		pump_pin = pin
		print(pump_pin)
		#GPIO.setup(pump_pin, GPIO.OUT, initial = GPIO.LOW)

		# step 1, 抽水 10sec
		#GPIO.output(pump_pin, GPIO.HIGH) # Turn on
		time.sleep(t1)
		print(t1)
		#GPIO.output(pump_pin, GPIO.LOW) # Turn off
        #GPIO.cleanup()
        #sys.exit()

	def up_photo(self):
		#os.system("python3 stepmotor.py --rotate %s" %rotate_number2)
		#arch = subprocess.check_output("python3 print.py", shell=True);
		#print(arch)
		os.system("docker run --rm -d --device /dev/camera1:/dev/camera1 -v /home/pi/capture-workspace:/tmp/capture-workspace -e \"TZ=Asia/Taipei\" --name capture jadezzz/capture-tools:latest")
		os.system("docker exec capture python3 capture.py -c /dev/camera1 -s \"1600x1200\"")
		os.system("docker exec capture python3 upload.py -u \"http://140.116.246.178:7777/upload/folder/shrimp/1\" -m \"folder\"")

if __name__ == "__main__":
	s = Rpi_photo(1,2)
	s.pump(8,1)
	time.sleep(6)
	s.up_photo()



