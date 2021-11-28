FROM tiangolo/uwsgi-nginx-flask
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install RPi.GPIO
RUN pip install -r /var/www/requirements.txt