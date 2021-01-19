from flask import Flask
from json import load
import os

paktmonitor = Flask("paktmonitor", static_folder="static/")

with open("settings.json") as settings:
    data = load(settings)
    for key in data:
        paktmonitor.config[key] = data[key]

from paktmonitor.client.routes import *
from paktmonitor.oauth.routes import *
from paktmonitor.api.routes import *