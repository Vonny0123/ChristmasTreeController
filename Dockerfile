FROM python:3.6-slim-stretch 
COPY . .
RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]