import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
import json

button_gpio = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pressed = False

end = 0
start = 0
total = 0
def callback_1(channel):
    global end
    global start
    global total
    if GPIO.input(21):
        end = time.time()
        print("end: "+str(end))
        total = end - start
        print("total :" + str(total))
    else:
        start = time.time()
        print("start: "+str(start))

GPIO.add_event_detect(21, GPIO.BOTH, callback = callback_1, bouncetime = 100)
while True:
    if total > 0 and total < 5:
        with open('/home/pi/Desktop/Raspberry-Pi-master/data.json', 'r') as js:
            dic = json.load(js)
            #dic['time1'] = dic['time1'] 
            dic['time2'] = 5
            #dic['deviceid'] = dic['deviceid']
        os.remove("/home/pi/Desktop/Raspberry-Pi-master/data.json")
        with open('/home/pi/Desktop/Raspberry-Pi-master/data.json', 'w') as js:
            json.dump(dic, js, indent = 4)
        os.system("python3 /home/pi/Desktop/Raspberry-Pi-master/rpi_gpio.py")
        #print("short pressed")
        total= 0
    elif total >=5:
        with open('/home/pi/Desktop/Raspberry-Pi-master/data.json', 'r') as js:
            dic = json.load(js)
            #dic['time1'] = dic['time1'] 
            dic['time2'] = 120
            #dic['deviceid'] = dic['deviceid']
        os.remove("/home/pi/Desktop/Raspberry-Pi-master/data.json")
        with open('/home/pi/Desktop/Raspberry-Pi-master/data.json', 'w') as js:
            json.dump(dic, js, indent = 4)
        os.system("python3 /home/pi/Desktop/Raspberry-Pi-master/rpi_gpio.py")
        #print("long pressed")
        total= 0
    
        

        
            




