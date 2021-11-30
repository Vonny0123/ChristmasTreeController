FROM python:3.6-slim-stretch 
COPY . .
RUN apt-get install RPi.GPIO
RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]