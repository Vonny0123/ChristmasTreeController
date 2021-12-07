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
    return render_template("home.html")


# I've added this method to receive slider updates
@app.route("/brightness_slider", methods=["POST", "GET"])
def slider():
    received_data = request.data
    tree.brightness = int(received_data) / 100
    return received_data


@app.route("/on_button", methods=["POST", "GET"])
def on_button():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
    received_data = request.data
    tree.on()
    return received_data


@app.route("/off_button", methods=["POST", "GET"])
def off_button():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
    received_data = request.data
    tree.off()
    return received_data


@app.route("/cycle_button", methods=["POST", "GET"])
def cycle_button():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
    received_data = request.data
    hue_cycle()
    return received_data


@app.route("/one_by_one_button", methods=["POST", "GET"])
def one_by_one_button():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
    received_data = request.data
    one_by_one()
    return received_data


@app.route("/sparkle_button", methods=["POST", "GET"])
def sparkle_button():
    exit_event1.set()
    exit_event2.set()
    exit_event3.set()
    received_data = request.data
    random_sparkles()
    return received_data


def hue_cycle():
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
