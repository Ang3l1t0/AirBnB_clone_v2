#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Hello Flask"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """route hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
