from flask import render_template, session, redirect, request, url_for
from application import app
from application.models import author

# TODO : MAKE auth_required DECORATOR
def auth_required(func) :
	def core(*args, **kwargs) :
		if session['author'] is None :
			return None
		else :
			return func(*args, **kwargs)
	return core