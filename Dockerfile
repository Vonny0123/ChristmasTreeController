FROM ubuntu:18.04
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get upgrade -y && apt-get install -y python python-pip curl
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
Copy ./app /app
COPY ./main.py /main.py
RUN pip install -r /var/www/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]