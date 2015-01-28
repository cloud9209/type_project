# -*- coding: utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, jsonify
from application.models import author
import logging

@app.route('/sign_in', methods=['POST'])
def sign_in() :
    if not author.verified(request.form) :
        return jsonify( success = False, action = 'alert', body = 'SignIn Failure' )
    _author = author.get('email', request.form['email'], 1)
    session['author_id'       ] = _author.id
    session['author_name'     ] = _author.name
    session['author_email'    ] = _author.email
    session['author_thumbnail'] = _author.thumbnail
    return jsonify( success = True, action = 'redirect', body = url_for('main', category = 'all'))

@app.route('/sign_up', methods=['POST'])
def sign_up() :
    success = author.add_exclusive(request.form)
    if not success : return jsonify( success = False, action = 'alert', body = 'SignUp Failure : E-mail Duplication' )
    else           : return jsonify( success =  True, action = 'alert', body = 'SignUp Success' )

@app.route('/sign_out')
def sign_out() :
    session.clear()
    return redirect(url_for('index'))