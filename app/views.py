from src.tree import RGBXmasTree
from colorzero import Color, Hue
from flask import Flask, render_template, request, redirect
import random
from threading import Thread, Event
from . import app, tree

exit_event1 = Event()
exit_event2 = Event()
exit_event3 = Event()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template(
            "home.html", brightness=int(request.form.get("brightness"))
        )
    elif request.method == "GET":
        return render_template("home.html")


# I've added this method to receive slider updates
@app.route("/slider_update", methods=["POST", "GET"])
def slider():
    received_data = request.data
    tree.brightness = int(received_data) / 100
    return received_data


@app.route("/on_click", methods=["POST", "GET"])
def slider():
    received_data = request.data
    halt_execution()
    tree.on()
    return received_data


@app.route("/off_click", methods=["POST", "GET"])
def slider():
    received_data = request.data
    tree.off()
    return received_data


@app.route("/sparkle_click", methods=["POST", "GET"])
def slider():
    received_data = request.data
    random_sparkles()
    return received_data


@app.route("/one_by_one_click", methods=["POST", "GET"])
def slider():
    received_data = request.data
    one_by_one()
    return received_data


@app.route("/cycle_click", methods=["POST", "GET"])
def slider():
    received_data = request.data
    hue_cycle()
    return received_data


def hue_cycle():
    halt_execution()
    tree.color = Color("red")
    if exit_event1.is_set():
        exit_event1.clear()
    try:
        while True:
            tree.color += Hue(deg=1)
            if exit_event1.is_set():
                break
    except KeyboardInterrupt:
        tree.close()


def one_by_one():
    halt_execution()
    colors = [Color("red"), Color("green"), Color("blue")]  # add more if you like
    if exit_event2.is_set():
        exit_event2.clear()
    try:
        while True:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
                    if exit_event2.is_set():
                        break
                else:
                    continue
                break
            else:
                continue
            break
    except KeyboardInterrupt:
        tree.close()


def random_sparkles():
    halt_execution()
    if exit_event3.is_set():
        exit_event3.clear()

    def random_color():
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)

    try:
        while True:
            pixel = random.choice(tree)
            pixel.color = random_color()
            if exit_event3.is_set():
                break
    except KeyboardInterrupt:
        tree.close()


def halt_execution():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
