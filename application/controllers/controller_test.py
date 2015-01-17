# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app
from application.models import author
import logging

# @app.route('/test')
# def test():
# 	proj_items = model_test.get_main_data()
# 	return render_template("test/test.html", proj_items = proj_items)

# @app.route('/test/get')
# def test_get() :
# 	proj_items = author_manager.get_proj_items(10)
# 	logging.info(proj_items)
# 	return render_template("main.html", proj_items = proj_items)

# @app.route('/test/init')
# def test_init() :
# 	author_manager.init_proj_items()
# 	return ""

