from application import app
from flask import session, request, redirect, url_for, jsonify, render_template
from application.models import work_comment, auth
import logging

@app.route('/work_comment/new', methods = ['POST'])
@auth.requires(auth.type.author)
def work_comment_new() :
    try :
        comment = work_comment.add(writer_id = session['author_id'], work_id = session['work_id'], body = request.form['body'])
        return jsonify( success = True, body = render_template('work_comment.html', comment = comment))
    except :
        raise
        return jsonify( success = False )

@app.route('/work_comment/<int:comment_id>/modify', methods = ['POST'])
@auth.requires(auth.type.work_comment)
def work_comment_modify(comment_id) :
    try :
        comment = work_comment.get('id', comment_id, 1)
        return jsonify( success = True, body = render_template('work_comment.html', comment = comment, input_mode = True))
    except :
        raise
        return jsonify( success = False )

@app.route('/work_comment/<int:comment_id>/submit', methods = ['POST'])
@auth.requires(auth.type.work_comment)
def work_comment_submit(comment_id) :
    try :
        comment = work_comment.modify(comment_id, request.form['body'])
        return jsonify( success = True, body = render_template('work_comment.html', comment = comment))
    except : 
        raise
        return jsonify( success = False )

@app.route('/work_comment/<int:comment_id>/remove', methods = ['POST'])
@auth.requires(auth.type.work_comment)
def work_comment_remove(comment_id) :
    try :
        work_comment.remove(comment_id)
        return jsonify( success = True )
    except :
        raise
        return jsonify( success = False )