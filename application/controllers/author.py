#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session
from application.models import author, auth
import logging

@app.route('/<int:author_id>')
@auth.requires(auth.type.signin)
def author_page(author_id) :
    session['author_id'] = author_id
    authors = author.get() # for navbar
    _author_ = author.get('id', author_id, 1)
    return render_template('author_page.html', author = _author_, authors = authors)