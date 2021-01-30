from logging import log
from paktmonitor.oauth.routes import login
from paktmonitor.client import client
from flask import redirect, url_for
@client.route("/")
def login():
    return redirect("/oauth/login")