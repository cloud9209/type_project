# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app
from application.models import model_test, author_manager
import logging

@app.route('/test')
def test():
	proj_items = model_test.get_main_data()
	return render_template("test/test.html", proj_items = proj_items)

@app.route('/test/get')
def test_get() :
	proj_list = author_manager.get_proj_list(10)
	logging.info(proj_list)
	return render_template("test/test.html", proj_items = proj_list)

@app.route('/test/init')
def test_init() :
	return author_manager.init_proj_list()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')