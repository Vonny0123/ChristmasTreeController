FROM ubuntu:20.04
RUN apt-get update --allow-unauthenticated && apt-get upgrade -y && apt-get install -y python3 python3-pip curl
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

