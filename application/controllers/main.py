#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect
from application.models import author, project_manager
import logging

@app.route('/')
def index(failure = False, message = "") :
	return render_template('index.html', failure = failure, message = message)

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in() :
	if request.method != 'POST' :
		return redirect(url_for('index'))
	if not author.verified(request.form) :
		logging.info("LOGIN FAILED")
		return redirect(url_for('index', failure = True, message = "Sign-in failure due to a wrong password."))
	logging.info("LOGIN SUCCESS")
	_author = author.get('email', request.form['email'], 1)
	session['author_id'] = _author.id
	session['author_email'] = _author.email
	return redirect(url_for('main'))

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up() :
	if request.method != 'POST' :
		return redirect(url_for('index'))
	success = author.add_exclusive(request.form)
	logging.info(["Not Added","Added Exclusively"][success])
	if not success :
		redirect(url_for('index', failure = True, message = "Sign-up failure due to e-mail duplication"))
	else :
		redirect(url_for('index', message = 'Sign-up Success'))

#@auth_required
@app.route('/main/<string:category>', defaults = {'category' : 'all'})
def main(category) :
	projects = None
	if category == 'all' :
		projects = project_manager.get_proj_items(10)
	elif category == 'reading' or category == 'displaying' :
		projects = project.get('category', category.upper(), 10)
	else :
		projects = project.get('author', category, 10)

	if projects == None : 
		raise
	else :
		render_template('main.html', projects = projects)


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