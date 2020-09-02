#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def closedb():
    """Close db session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route states_list"""
    states = storage.all(state)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
