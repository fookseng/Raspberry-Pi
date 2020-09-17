import RPi.GPIO as GPIO
from gpiozero import LED
import RPistepper as stp
import time, sys
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-r", "--rotate", default = 1,
#     help="Number of rotation")
# args = vars(ap.parse_args())

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED
LED_PIN = 8
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
#light up LED for 9sec
i = 9
while i > 0: 
    GPIO.output(8, GPIO.HIGH) # Turn off
    time.sleep(1)             # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)  # Turn on
    time.sleep(1)
    i = i - 1
#########################
# gpiozero library usage
#led = LED(2)
#led.on()
#########################
GPIO.cleanup()
sys.exit()