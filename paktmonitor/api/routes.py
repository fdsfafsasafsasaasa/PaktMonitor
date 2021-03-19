from flask import render_template, request
from flask_login import login_required
from paktmonitor.api.models import User
from paktmonitor.api import api
import json

@api.route("login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = User.login_user(request.form.get("username"), request.form.get("password"))
        if not user:
            return render_template("login.html")
        return render_template("user.html", user=user)

@api.route("appliances/status")
def appliances_status():
    return json.dumps([
        {
            "name": "Toshiba Fridge",
            "current_usage": 15,
            "average_usage": 50,
            "lowest_usage": 0
        },
        {
            "name": "Whirlpool Television",
            "current_usage": 10,
            "average_usage": 5,
            "lowest_usage": 0
        }
    ])

@api.route("appliances/update/<uuid>")
def appliance_update(uuid):
    pass