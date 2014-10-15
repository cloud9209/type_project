from flask import Flask, render_template

app = Flask(__name__)

# -*- coding: utf-8 -*-


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('type_index.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

