# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app
from application.models import model_test

@app.route('/test')
def test():
	proj_items = model_test.get_main_data()
	return render_template("test/test.html", proj_items = proj_items)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')