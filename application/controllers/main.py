#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import signin, author, project, auth, work
import logging

@app.route('/')
def index() :
    if signin.secure().safe : return redirect(url_for('main'))
    return render_template('index.html')

project_category = ['reading', 'displaying', 'lettering']
@app.route('/main/', defaults = {'category' : 'all'})
@app.route('/main/<string:category>')
@auth.requires(auth.type.signin)
def main(category) :
    projects = None
    if   category == 'all'            : projects = project.get(limit = 10)
    elif category in project_category : projects = project.get('category', category.upper(), 10)
    else                              : projects = project.get('author_id', int(category), 10)
    if projects is None : abort(404)
    return render_template('main.html', projects = projects)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')