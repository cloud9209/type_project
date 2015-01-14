# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app
from application.models import model_test, author_manager

@app.route('/test')
def test():
	proj_items = model_test.get_main_data()
	return render_template("test/test.html", proj_items = proj_items)

@app.route('/test/get')
def test_get() :
	return model_test.get_proj_list(10)

@app.route('/test/init')
def test_init() :
	return model_test.init_proj_list()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')