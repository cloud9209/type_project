# -*- coding: utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect
from application.models import author
import logging

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in() :
    if request.method != 'POST' :
        return redirect(url_for('index'))
    if not author.verified(request.form) :
        logging.info("LOGIN FAILED")
        session['msg-index'] = "Sign-in failure due to a wrong password."
        return redirect(url_for('index'))
    logging.info("LOGIN SUCCESS")
    _author = author.get('email', request.form['email'], 1)
    session['author_id'] = _author.id
    session['author_name'] = _author.name
    session['author_email'] = _author.email
    return redirect(url_for('main', category = 'all'))

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up() :
    if request.method != 'POST' :
        return redirect(url_for('index'))
    
    success = author.add_exclusive(request.form)
    logging.info(["Not Added","Added Exclusively"][success]) # LOGGING

    # to index with message
    if not success : session['msg-index'] = "Sign-up failure due to e-mail duplication"
    else           : session['msg-index'] = 'Sign-up Success'
    return redirect(url_for('index'))

@app.route('/sign_out')
def sign_out() :
    session.clear()
    return redirect(url_for('index'))