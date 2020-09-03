from flask import Flask

from shop import app, db


@app.route('/')
def index():
    return "Home Page"
