#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session
from application.models import author, auth

# is the author page for owner, or for everyone??
@app.route('/<int:author_id>')
@auth.requires(auth.type.signin)
def author_page(author_id) :
    session['author_id'] = author_id
    _author_ = author.get('id', author_id, 1)
    return render_template('author_page.html', author = _author_)