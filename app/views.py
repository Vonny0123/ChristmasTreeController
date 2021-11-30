from colorzero import Color, Hue
from flask import Flask, render_template, request
import random
from threading import Thread, Event
from . import app, tree

exit_event = Event()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        exit_event.set()

        if request.form.get("On") == "On":
            tree.on()
            return render_template("home.html")
        elif request.form.get("Off") == "Off":
            tree.off()
            return render_template("home.html")
        elif request.form.get("Cycle") == "On":
            thread = Thread(target=hue_cycle)
            thread.daemon = True
            thread.start()
            return render_template("home.html")
        elif request.form.get("OneByOne") == "On":
            thread = Thread(target=one_by_one)
            thread.daemon = True
            thread.start()
            return render_template("home.html")
        elif request.form.get("Sparkle") == "On":
            thread = Thread(target=random_sparkles)
            thread.daemon = True
            thread.start()
            return render_template("home.html")
        else:
            return "Error"
    elif request.method == "GET":
        return render_template("home.html")

    return render_template("home.html")


def hue_cycle():
    tree.color = Color("red")

    try:
        while True:
            tree.color += Hue(deg=1)
            if exit_event.is_set():
                break
    except KeyboardInterrupt:
        tree.close()


def one_by_one():
    colors = [Color("red"), Color("green"), Color("blue")]  # add more if you like

    try:
        while True:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
            if exit_event.is_set():
                break
    except KeyboardInterrupt:
        tree.close()


def random_sparkles():
    def random_color():
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)

    try:
        while True:
            pixel = random.choice(tree)
            pixel.color = random_color()
            if exit_event.is_set():
                break
    except KeyboardInterrupt:
        tree.close()
