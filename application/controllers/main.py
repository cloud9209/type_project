#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect
from application.models import author, project_manager
import logging

@app.route('/')
def index(signin_failed = False) :
	return render_template('index.html', failed_sign_in = signin_failed)

@app.route('/sign_in')
def sign_in() :
	if request.methos != 'POST' :
		return redirect(url_for('index'))
	if not author.verified(request.form) :
		return redirect(url_for('index', signin_failed = True))
	_author = author.get('email', request.form['email'])
	session['author_id'] = _author.id
	session['author_email'] = _author.email
	return redirect(url_for('main'))

#@auth_required
@app.route('/main')
def main() :
	projects = project_manager.get_proj_items(10)
	return render_template("main.html", projects = projects)


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

# @app.route('/signup', methods = ['GET', 'POST'])
# def sign_up() :
# 	if request.method == 'POST' :
# 		_author = author.add_exclusively(request.form)
# 		return redirect( url_for('/') )

# @app.route('/signout')
# def sign_out() :
# 	session.clear()
# 	return redirect(url_for('/'))

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')