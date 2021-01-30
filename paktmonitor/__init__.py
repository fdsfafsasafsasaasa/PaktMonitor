from flask import Flask
from json import load
import os

paktmonitor = Flask("paktmonitor", static_folder="static/")
paktmonitor.secret_key = b"99754106633f94d350db34d548d6091a"
with open("settings.json") as settings:
    data = load(settings)
    for key in data:
        paktmonitor.config[key] = data[key]

from paktmonitor.views import *