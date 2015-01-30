#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify, send_file
from application.models import project, auth, work, project_comment, project_like, author, image_storage
import logging

@app.route('/project/<int:project_id>/register', methods = ['POST'])
@auth.requires(auth.type.project)
def register_project(project_id) :
    if session['project_id'] != project_id : abort(404) # invalid project number
    _project = project.get('id', project_id, 1)
    work.add_project_copy(_project) # -> work.add(data)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>/like', methods = ['POST'])
@auth.requires(auth.type.author)
def like_project(project_id) :
    try :
        like_now   = project_like.toggle(liker_id = session['author_id'], project_id = project_id)
        like_count = len(project_like.get('project_id', project_id))
        return jsonify( success = True, count = like_count, like = like_now)
    except :
        return jsonify( success = False, action = 'alert', body = 'Like Action Failed' )

@app.route('/project/<int:project_id>/delete', methods = ['POST'])
@auth.requires(auth.type.author)
def delete_project(project_id) :
    if session['project_id'] != project_id : abort(404) # invalid project number
    _project = project.remove('id', project_id, 1)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@auth.requires(auth.type.author)
def type_project(project_id) :
    session['project_id'] = project_id

    _project_ = project.get('id', project_id, 1)
    if _project_ is None : abort(404)

    authors = author.get()
    return render_template('project.html', project = _project_, authors = authors)

@app.route('/project/<int:project_id>/description', methods=['POST'])
#@auth.requires(auth.type.project)
def project_description(project_id) :
    if 'body' in request.form : # modify
        _project_ = project.set(project_id, 'description', request.form['body'])
        return jsonify( success = True, action = None, body = render_template('description.html', input_mode = False, description = _project_.description))
    else :
        _project_ = project.get('id', project_id, 1)
        return jsonify( success = True, action = None, body = render_template('description.html', input_mode = True, description = _project_.description))
