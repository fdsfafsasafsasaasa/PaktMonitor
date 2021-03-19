from flask_login import LoginManager
from flask import Flask, app
from json import load

paktmonitor = Flask("paktmonitor", static_folder="static/")
paktmonitor.secret_key = b"99754106633f94d350db34d548d6091a"
login_manager = LoginManager()
login_manager.init_app(paktmonitor)
with open("settings.json") as settings:
    data = load(settings)
    for key in data:
        paktmonitor.config[key] = data[key]

from paktmonitor.views import *