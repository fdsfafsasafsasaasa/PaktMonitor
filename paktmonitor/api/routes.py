from flask import render_template, request, redirect
from paktmonitor.api.models import User
from paktmonitor.api import api
from uuid import uuid4

api.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if request.cookies.get("session_id"):
            return redirect("/user")
        return render_template("login.html")
    elif request.method == "POST":
        user = User(
            request.form.get("username"),
            uuid4(),
            request.form.get("password")
        )
        response = make_response(render_template("user.html", user=user))
        response.set_cookie('session_id', str(user.session_uuid))
        return response