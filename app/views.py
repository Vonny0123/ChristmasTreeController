from flask import Flask, render_template, request
from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("On") == "On":
            return "1"
        elif request.form.get("Off") == "Off":
            return "2"
        else:
            return "3"
    elif request.method == "GET":
        return render_template("home.html")

    return render_template("home.html")
