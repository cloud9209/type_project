from application import app
from flask import session, request, redirect, url_for, jsonify, render_template
from application.models import project_comment, work_comment
import logging

@app.route('/submit_project_comment', methods = ['POST'])
def submit_project_comment() :
    logging.debug('request method : ' + request.method)
    if request.method != 'POST' : return
    try :
        comment = project_comment.add(writer_id = session['author_id'], project_id = session['project_id'], body = request.form['body'])
        logging.debug(render_template('comment_proj.html', comment = comment))
        return jsonify( success = True, body = render_template('comment_proj.html', comment = comment))
    except :
        return jsonify( success = False )

@app.route('/submit_work_comment', methods = ['POST'])
def submit_work_comment() :
    if request.method != 'POST' : return
    work_comment.add(writer_id = session['author_id'], work_id = session['work_id'], body = request.form['body'])
    return redirect(url_for('type_work', work_id = session['work_id']))