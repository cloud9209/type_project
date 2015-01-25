#_*_ coding:utf_8 _*_
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify
from application.models import work, auth, work_comment, work_like, storage_handler
import logging

@app.route('/work/<int:work_id>', methods = ['GET', 'POST'])
@auth.requires(auth.type.author)
def type_work(work_id) :
    session['work_id'] = work_id

    __work__ = work.get('id', work_id, 1)
    if __work__ is None : abort(404)

    return render_template('work.html', work = __work__)

@app.route('/work/<int:work_id>/like', methods = ['POST'])
@auth.requires(auth.type.author)
def like_work(work_id) :
    try :
        like_count = work_like.toggle(liker_id = session['author_id'], work_id = work_id)
        return jsonify( success = True, count = like_count)
    except :
        raise
        return jsonify( success = False )

@app.route('/work/<int:work_id>/upload', methods = ['POST'])
def upload_work_image(work_id) :
    storage_handler.store_work_image(work_id, request.files['uploading-image'])
    return redirect(url_for('type_work', work_id = work_id))

@app.route('/image/work/<path:filename>')
def load_work_image(filename) :
    return storage_handler.load_work_image(filename)