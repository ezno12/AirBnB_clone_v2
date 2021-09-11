#!/usr/bin/python3
"""
0-hell_route - starts a Flask web app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ outputs 'Hello HBNB!' """
    app.url_map.strict_slashes = False
    return 'Hello, HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
