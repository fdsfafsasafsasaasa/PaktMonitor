from flask import render_template, request, redirect, make_response
from paktmonitor.api.models import User
from paktmonitor.api import api
from uuid import uuid4
import json

@api.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if request.cookies.get("session_id"):
            return redirect("/user")
        return render_template("login.html")
    elif request.method == "POST":
        user = User.login_user(request.form.get("username"), request.form.get("password"))
        response = make_response(render_template("user.html", user=user))
        response.set_cookie('session_id', str(user.session_uuid))
        return response

@api.route("/appliances/status")
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

@api.route("/appliances/update/<uuid>")
def appliance_update(uuid):
    pass