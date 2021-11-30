FROM python:3.6-slim-stretch 
COPY . .
RUN pip install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]