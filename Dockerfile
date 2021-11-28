FROM python:3.8
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./requirements.txt .
Copy ./app .
COPY ./main.py .
RUN pip install -r /requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]