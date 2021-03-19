from paktmonitor.api.routes import login
from flask import request, render_template
from paktmonitor.api.models import User
from flask_login import login_required
from paktmonitor.client import client

@client.route("login")
def root():
    return render_template("index.html")

@login_required
@client.route("dashboard")
def dashboard():
    return render_template("dashboard.html", user=User.get_user(request.cookies.get("uuid")))