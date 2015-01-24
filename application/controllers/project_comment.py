from application import app
from flask import session, request, redirect, url_for, jsonify, render_template
from application.models import project_comment, work_comment, auth
import logging

@app.route('/project_comment/new', methods = ['POST'])
@auth.requires(auth.type.author)
def project_comment_new() :
    try :
        comment = project_comment.add(writer_id = session['author_id'], project_id = session['project_id'], body = request.form['body'])
        logging.debug(render_template('project_comment.html', comment = comment))
        return jsonify( success = True, body = render_template('project_comment.html', comment = comment))
    except :
        raise
        return jsonify( success = False )

@app.route('/project_comment/<int:comment_id>/modify', methods = ['POST'])
@auth.requires(auth.type.project_comment)
def project_comment_modify(comment_id) :
    comment = project_comment.get('id', comment_id, 1)
    logging.debug(render_template('project_comment_input.html', comment = comment))
    try :
        #comment = project_comment.get('id', comment_id, 1)
        return jsonify( success = True, body = render_template('project_comment_input.html', comment = comment))
    except :
        return jsonify( success = False )

@app.route('/project_comment/<int:comment_id>/submit', methods = ['POST'])
@auth.requires(auth.type.project_comment)
def porject_comment_submit(comment_id) :
    try :
        comment = project_comment.modify(comment_id, request.form['body'])
        return jsonify( success = True, body = render_template('project_comment.html', comment = comment))
    except : 
        return jsonify( success = False )

@app.route('/project_comment/<int:comment_id>/remove', methods = ['POST'])
@auth.requires(auth.type.project_comment)
def project_comment_remove(comment_id) :
    try :
        project_comment.remove(comment_id)
        return jsonify( success = True )
    except :
        return jsonify( success = False )