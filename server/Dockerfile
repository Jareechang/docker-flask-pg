FROM python:2.7
MAINTAINER Jerry Chang "therealjerrycan@gmail.com"

ADD . /server
WORKDIR /server

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -r requirements.txt

CMD python run.py 
