FROM arm32v6/alpine
RUN apk add --no-cache python3 py3-pip
RUN python3 -m ensurepip
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt