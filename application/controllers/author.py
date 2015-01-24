#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify
from application.models import author, auth
import logging

@app.route('/<int:author_id>')
@auth.requires(auth.type.author)
def author_page(author_id) :
    authors = author.get()
    return render_template('author_page.html', authors = authors)