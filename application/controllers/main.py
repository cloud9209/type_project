#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import author, project, auth
from functools import wraps
import logging

@app.route('/')
def index() :
	# secure : logged-in // main/all -> if possible, return where it was.
	if auth.secure() : return redirect(url_for('main', category = 'all'))

	message = session.pop('msg-index', "")
	return render_template('index.html', message = message)

@app.route('/main/<string:category>')
@auth.required # 404 if not authorized
def main(category) :
	projects = None
	if   category == 'all'                    : projects = project.get(limit = 10)
	elif category in ['reading','displaying'] : projects = project.get('category', category.upper(), 10)
	else : # category is author_id
		try :
			author.get('id', int(category), 1)
			projects = project.get('author_id', int(category), 10)
			logging.info("Success : " + category)
		except ValueError :
			pass
		except : # sqlalchemy.orm.exc.NoResultFound or MultipleResultFound
			pass

	if projects == None : abort(404)
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