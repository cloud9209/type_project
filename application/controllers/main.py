#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect
from application.models import author, project
from functools import wraps
import logging, auth

@app.route('/')
def index() :
	if 'msg-index' in session :
		message = session['msg-index']
		session.pop('msg-index', None)
		return render_template('index.html', message = message)
	else :
		return render_template('index.html', message = "")

@app.route('/main/<string:category>')
@auth.required # 404 if not authorized
def main(category) :
	projects = None
	logging.info(str(category))
	if   category == 'all'                    : projects = project.get(limit = 10)
	elif category in ['reading','displaying'] : projects = project.get('category', category.upper(), 10)
	else                                      : projects = project.get('author', category, 10)

	if projects == None : raise
	return render_template('main.html', projects = projects)

@app.route('/inside_proj', methods=['GET', 'POST'])
def inside_proj():
	paper_items = [
		{
			'date' : u"2014년 6월 7일 14시 20분", 
			'image' : 'res/images/process_test_6.jpg',
			'description' : u"어려웧ㅎㅎ"
		}, {
			'date' : u"2014년 6월 7일 14시 20분", 
			'image' : 'res/images/process_test_6.jpg',
			'description' : u"어려웧ㅎㅎ"
		}, {
			'date' : u"2014년 6월 7일 14시 20분", 
			'image' : 'res/images/process_test_6.jpg',
			'description' : u"어려웧ㅎㅎ"
		}, {
			'date' : u"2014년 6월 7일 14시 20분", 
			'image' : 'res/images/process_test_6.jpg',
			'description' : u"어려웧ㅎㅎ"
		}, {
			'date' : u"2014년 6월 7일 14시 20분", 
			'image' : 'res/images/process_test_6.jpg',
			'description' : u"어려웧ㅎㅎ"
		}		
	]
	return render_template('inside_proj_item.html', history = paper_items, likes = [], comments = [])

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')