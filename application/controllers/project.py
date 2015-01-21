
#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import project, auth, work, project_comment
import logging

@app.route('/project/<int:project_id>/register', methods = ['POST'])
@auth.required # 404 if not authorized
def register_project(project_id) :
    if session['project-id'] != project_id : abort(404) # invalid project number
    _project = project.get('id', project_id, 1)
    work.add_project_copy(_project) # -> work.add(data)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>/delete', methods = ['POST'])
@auth.required # 404 if not authorized
def delete_project(project_id) :
    if session['project-id'] != project_id : abort(404) # invalid project number
    _project = project.remove('id', project_id, 1)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@auth.required # 404 if not authorized
def type_project(project_id) :
    session['project-id'] = project_id

    __project__ = project.get('id', project_id, 1)
    if __project__ is None : abort(404)

    return render_template('project.html', project = __project__)