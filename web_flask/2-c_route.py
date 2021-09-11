#!/usr/bin/python3
"""
2-c_roiute - starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ outputs 'Hello HBNB!' """
    app.url_map.strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ outputs 'HBNB' """
    app.url_map.strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ outputs 'C <text> """
    text = text.replace('_', ' ')

    app.url_map.strict_slashes = False
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
