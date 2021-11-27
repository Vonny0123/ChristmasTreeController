from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("on") == "on":
            pass  # do something
        elif request.form.get("off") == "off":
            pass  # do something else
        else:
            pass  # unknown
    elif request.method == "GET":
        return render_template("home.html", form=form)

    return render_template("home.html")
