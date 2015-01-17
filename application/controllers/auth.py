from flask import render_template, session, redirect, request, url_for
from application import app
from application.models import author_manager

# TODO : MAKE auth_required DECORATOR

@app.route('/login', methods = ['GET', 'POST'])
def login() :
	if request.method == 'POST' :

@app.route('/signout')
def sign_out() :
	session.pop('logged_in', None)
	session.pop('email', None)
	return redirect(url_for('layout'))

def auth_required(func) :
	def core(*args, **kwargs) :
		if session['author'] is None :
			return None
		else :
			return func(*args, **kwargs)
	return core