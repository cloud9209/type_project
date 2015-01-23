from application import app
from flask import session, request, redirect, url_for
from application.models import project_comment, work_comment

@app.route('/submit_project_comment', methods = ['POST'])
def submit_project_comment() :
    if request.method != 'POST' : return
    project_comment.add(writer_id = session['author_id'], project_id = session['project_id'], body = request.form['body'])
    return redirect(url_for('type_project', project_id = session['project_id']))

@app.route('/submit_work_comment', methods = ['POST'])
def submit_work_comment() :
    if request.method != 'POST' : return
    work_comment.add(writer_id = session['author_id'], work_id = session['work_id'], body = request.form['body'])
    return redirect(url_for('type_work', work_id = session['work_id']))