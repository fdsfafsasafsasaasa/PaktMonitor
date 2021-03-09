FROM debian:buster

RUN apt install -y python-pymongo python-flask

RUN git clone https://github.com/thewarsawpakt/PaktMonitor