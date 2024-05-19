#!/usr/bin/python3
"""
This module starts a Flask web application with specified routes.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Route to display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route to display 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Route to display 'C ' followed by the value of the text variable """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
