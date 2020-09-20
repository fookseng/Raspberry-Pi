import json
import os

time_list = []

time_list.append("@reboot sleep 180 && python3 /home/pi/Desktop/Raspberry-Pi-master/button.py &")
time_list.append("@reboot sleep 120 && python3 /home/pi/Desktop/Raspberry-Pi-master/rpi_gpio.py")
time_list.append("0"+ " "+"* "+"* "+"* "+"* "+ "python3 /home/pi/Desktop/Raspberry-Pi-master/rpi_gpio.py")

output = open("cron_file.txt", "w")
for line in time_list:
    output.write(line)
    output.write("\n")
output.close()

os.system("crontab cron_file.txt")
