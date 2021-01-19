from flask import Flask
from json import load
import os

paktmonitor = Flask("paktmonitor", static_folder="static/")

with open("settings.json") as config:
    print(load(config))
    for key in load(config):
        paktmonitor.config[key] = config[key]