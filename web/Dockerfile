FROM python:2.7
MAINTAINER Jerry Chang "therealjerrycan@gmail.com"

ADD . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -r ./server/requirements.txt

CMD python run.py 
