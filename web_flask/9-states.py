#!/usr/bin/python3
"""
9-sates - starts a flask application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def get_states():
    """ displays an html page with states  """
    states = storage.all('State').values()
    state_count = len(states)

    return render_template('9-states.html', states=states,
                           state_count=state_count)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """ displays an html page with a single state  """
    states = storage.all('State')
    if id is None:
        return render_template('9-states.html', states=states.values)

    state = ""
    cities = []
    for k in states.keys():
        if id == k:
            state = states.get(k)
            cities = state.cities
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown(self):
    """ closes storage session """
    storage.close()

if __name__ == "__main__":
    """ runs application only if not being imported  """
    app.run(host='0.0.0.0', port=5000)
