#!/usr/bin/python3
"""
10-hbnb_filters - starts a flask application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters/', strict_slashes=False)
def hbnb_filters():
    """ displays an index.html page  """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()


    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities, cities=cities)


@app.teardown_appcontext
def teardown(self):
    """ closes storage session """
    storage.close()

if __name__ == "__main__":
    """ runs application only if not being imported  """
    app.run(host='0.0.0.0', port=5000)
