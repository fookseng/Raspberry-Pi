# Raspberry-Pi
Installation:
1. pip install RPi.GPIO
2. pip install RPistepper
3. sudo apt install python3-gpiozero / sudo pip3 install gpiozero
4. pip3 install ModbusTCP
5. run background simple-rtsp-server
6. push video : ffmpeg -f v4l2 -i /dev/camera1 -rtsp_transport tcp -f rtsp rtsp://localhost:8554/stream
