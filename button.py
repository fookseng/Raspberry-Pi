import RPi.GPIO as GPIO
import time
import os

if __name__ == "__main__":
    button_gpio = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pressed = False
    
    while True:
        if not GPIO.input(button_gpio):
            if not pressed:
                print("button pressed")
                pressed = True
                os.system("python3 rpi_gpio.py")
            else:
                pressed = False
            time.sleep(0.1)
            


