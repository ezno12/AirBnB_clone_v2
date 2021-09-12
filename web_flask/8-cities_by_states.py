#!/usr/bin/python3
"""
8-cities_by_state - starts a flask operation
"""
from flask import Flask, render_template
from os import environ
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ closes storage session  """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all('State').values()
    cities = storage.all('City').values()

    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
