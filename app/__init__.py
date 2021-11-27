from flask import Flask

app = Flask(__name__)
from app.src.tree import RGBXmasTree

tree = 1
from app import views
