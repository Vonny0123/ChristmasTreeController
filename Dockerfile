FROM resin/rpi-raspbian:latest
RUN apt-get -q update && \
	apt-get -qy install \
        python python-pip \
        python-dev python-pip gcc make  
COPY . .
RUN pip install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]