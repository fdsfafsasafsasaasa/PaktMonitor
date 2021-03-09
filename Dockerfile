FROM debian:buster

RUN apt update -y

RUN apt install -y python3 python3-pip git

RUN pip3 install pymongo flask flask_discord

RUN git clone https://github.com/thewarsawpakt/PaktMonitor

RUN cd PaktMonitor; python3 -m paktmonitor