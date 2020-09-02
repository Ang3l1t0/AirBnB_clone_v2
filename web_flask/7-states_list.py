#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb():
    """Close db session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route /states_list"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)



if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
