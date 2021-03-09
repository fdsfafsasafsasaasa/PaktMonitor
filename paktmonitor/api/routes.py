from flask import render_template, request, redirect
from paktmonitor.api.models import login_user
from paktmonitor.api import api

app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if request.cookies.get("session-id"):
            return redirect("/user")
        return render_template("login.html")
    elif request.method == "POST":
        uuid = uuid4()
        user = User(
            request.form.get("username"),
            uuid,
            request.form.get("password")
        )
        response = make_response(render_template("user.html", user=user))
        response.set_cookie('session_id', str(user.session_uuid))
        return response