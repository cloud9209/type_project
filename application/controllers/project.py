
#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify
from application.models import project, auth, work, project_comment, project_like, author
import logging

@app.route('/project/<int:project_id>/register', methods = ['POST'])
@auth.requires(auth.type.project) # 404 if not authorized
def register_project(project_id) :
    if session['project_id'] != project_id : abort(404) # invalid project number
    _project = project.get('id', project_id, 1)
    work.add_project_copy(_project) # -> work.add(data)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>/like', methods = ['POST'])
@auth.requires(auth.type.signed_in) # 404 if not authorized
def like_project(project_id) :
    success = False
    try :
        project_like.toggle(session['author_id'], project_id)
        success = True
    except :
        logging.debug("Like Assertion Failed")
        pass
    return jsonify(is_success = success, like_count = len(project_like.get('project_id', project_id)))

@app.route('/project/<int:project_id>/delete', methods = ['POST'])
@auth.requires(auth.type.signed_in) # 404 if not authorized
def delete_project(project_id) :
    if session['project_id'] != project_id : abort(404) # invalid project number
    _project = project.remove('id', project_id, 1)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@auth.requires(auth.type.signed_in) # 404 if not authorized
def type_project(project_id) :
    session['project_id'] = project_id

    __project__ = project.get('id', project_id, 1)
    if __project__ is None : abort(404)

    authors = author.get()
    return render_template('project.html', project = __project__, authors = authors)