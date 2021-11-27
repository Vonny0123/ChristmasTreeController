from flask import Flask, render_template, request
from app import app, tree


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("On") == "On":
            tree.on()
        elif request.form.get("Off") == "Off":
            tree.off()
        else:
            return "Error"
    elif request.method == "GET":
        return render_template("home.html")

    return render_template("home.html")
