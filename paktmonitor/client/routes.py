from flask import redirect, url_for, render_template
from paktmonitor.client import client

@client.route("login")
def root():
    return render_template("index.html")