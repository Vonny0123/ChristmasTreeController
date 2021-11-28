from flask import Flask

app = Flask(__name__)
from src.tree import RGBXmasTree

tree = 1
from app import views
