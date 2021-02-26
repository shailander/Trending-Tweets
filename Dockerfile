FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install flask
RUN pip3 install tweepy
RUN pip3 install camelcase

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/index.py flask run --host=0.0.0.0