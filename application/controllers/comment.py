from application import app
from flask import session, request, redirect, url_for
from application.models import project_comment

@app.route('/submit_project_comment', methods = ['POST'])
def submit_project_comment() :
    if request.method != 'POST' : return
    project_comment.add(writer_id = session['id'], project_id = session['project-id'], body = request.form['body'])
    return redirect(url_for('type_project', project_id = session['project-id']))