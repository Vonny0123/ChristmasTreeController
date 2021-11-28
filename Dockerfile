FROM arm32v6/alpine:3.6
RUN apk --no-cache add bash python python-dev py-pip build-base curl
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt