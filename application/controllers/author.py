#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify
from application.models import author, auth, storage_handler
import logging

@app.route('/<int:author_id>')
@auth.requires(auth.type.author)
def author_page(author_id) :
    authors = author.get()
    return render_template('author_page.html', authors = authors)

@app.route('/author/<int:author_id>/upload', methods = ['POST'])
def upload_author_image(author_id) :
    storage_handler.store_author_image(author_id, request.files['uploading-image'])
    return redirect(url_for('type_author', author_id = author_id))

@app.route('/image/author/<path:filename>')
def load_author_image(filename) :
    return storage_handler.load_author_image(filename)