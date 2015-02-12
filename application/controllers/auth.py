# -*- coding: utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, jsonify
from application.models import author, signin

# TODO : Signin With Google
@app.route('/sign_in', methods=['POST'])
def sign_in() :
    _author_ = signin.get_verified_user(request.form)
    if _author_ is None : return jsonify( success = False, action = 'alert', body = 'SignIn Failure' )
    
    # Signin Success
    session['user_id'       ] = _author_.id
    session['user_name'     ] = _author_.name
    session['user_email'    ] = _author_.email
    session['user_thumbnail'] = _author_.thumbnail
    next_url = request.referrer
    if next_url is None : raise # Initial Setting to Catch a BUG
    return jsonify( success = True, action = 'redirect', body = next_url)

@app.route('/sign_up', methods=['POST'])
def sign_up() :
    success = author.add_exclusive(request.form)
    if not success : return jsonify( success = False, action = 'alert', body = 'SignUp Failure : E-mail Duplication' )
    else           : return jsonify( success =  True, action = 'alert', body = 'SignUp Success' )

@app.route('/sign_out')
def sign_out() :
    session.clear()
    return redirect(url_for('index'))