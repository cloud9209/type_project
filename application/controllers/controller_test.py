# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app
from application.models import author_manager
import logging

# @app.route('/test')
# def test():
# 	proj_items = model_test.get_main_data()
# 	return render_template("test/test.html", proj_items = proj_items)

@app.route('/test/get')
def test_get() :
	proj_items = author_manager.get_proj_items(10)
	logging.info(proj_items)
	for item in proj_items :
		logging.info("name : " + str(item.name))
	return render_template("inside_proj_item.html", proj_items = proj_items)

# @app.route('/test/init')
# def test_init() :
# 	author_manager.init_proj_items()
# 	return ""

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')