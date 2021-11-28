FROM ubuntu:16.04
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip curl
RUN pip3 install --upgrade pip
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY ./main.py ./main.py
RUN pip3 install -r /var/www/requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]