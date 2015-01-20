#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import author, project, auth, work
import logging

@app.route('/')
def index() :
    # secure : logged-in // TODO : main/all -> if possible, return where it was.
    if auth.secure() : return redirect(url_for('main', category = 'all'))

    message = session.pop('msg-index', "")
    return render_template('index.html', message = message)

@app.route('/main/<string:category>')
@auth.required # 404 if not authorized
def main(category) :
    projects = None
    if   category == 'all'                    : projects = project.get(limit = 10)
    elif category in ['reading','displaying'] : projects = project.get('category', category.upper(), 10)
    else : # category is author_id
        try :
            author.get('id', int(category), 1)
            projects = project.get('author_id', int(category), 10)
            logging.info("Success : " + category)
        except ValueError :
            pass
        except : # sqlalchemy.orm.exc.NoResultFound or MultipleResultFound
            pass
    if projects == None : abort(404)

    authors = author.get()
    return render_template('main.html', projects = projects, authors = authors)

@app.route('/project/<int:project_id>/register', methods = ['GET', 'POST'])
@auth.required # 404 if not authorized
def register_project(project_id) :
    if session['project-id'] != project_id : abort(404) # invalid project number
    _project = project.get('id', project_id, 1)
    work.add_project_copy(_project) # -> work.add(data)
    return redirect(url_for('type_project', project_id = project_id))

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@auth.required # 404 if not authorized
def type_project(project_id) :
    session['project-id'] = project_id

    curr_project = project.get('id', project_id, 1)
    if curr_project is None : abort(404)

    history = work.get('project_id', project_id) # get all works within the project.
    return render_template('project.html', project = curr_project, history = history, likes = [], comments = [])

    # paper_items = [
    #     {
    #         'date' : u"2014년 6월 7일 14시 20분", 
    #         'image' : 'res/images/process_test_6.jpg',
    #         'description' : u"어려웧ㅎㅎ"
    #     }, {
    #         'date' : u"2014년 6월 7일 14시 20분", 
    #         'image' : 'res/images/process_test_6.jpg',
    #         'description' : u"어려웧ㅎㅎ"
    #     }, {
    #         'date' : u"2014년 6월 7일 14시 20분", 
    #         'image' : 'res/images/process_test_6.jpg',
    #         'description' : u"어려웧ㅎㅎ"
    #     }, {
    #         'date' : u"2014년 6월 7일 14시 20분", 
    #         'image' : 'res/images/process_test_6.jpg',
    #         'description' : u"어려웧ㅎㅎ"
    #     }, {
    #         'date' : u"2014년 6월 7일 14시 20분", 
    #         'image' : 'res/images/process_test_6.jpg',
    #         'description' : u"어려웧ㅎㅎ"
    #     }       
    # ]

@app.errorhandler(404)
def page_not_found(e):
    authors = []
    if auth.secure() : authors = author.get()
    return render_template('404.html', authors = authors)