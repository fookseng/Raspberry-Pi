FROM lsiobase/ffmpeg:arm32v7-bin as binstage
FROM lsiobase/ubuntu:arm32v7-bionic
# Add files from binstage
COPY --from=binstage / /
MAINTAINER Docker CFS 
RUN apt-get update
#RUN sudo apt install sudo
RUN pip3 install pyModbusTCP
RUN pip install RPI.GPIO
ADD append.txt /
ADD button.py /
ADD data.json /
ADD rpi_gpio.py /
CMD [ "python3", "./button.py" ]

