from flask import Flask

app = Flask(__name__)
from src.tree import RGBXmasTree

tree = RGBXmasTree()
from app import views
