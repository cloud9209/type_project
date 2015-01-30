#_*_ coding:utf_8 _*_
from application import app
from flask import render_template, session, url_for, request, redirect, abort, jsonify
from application.models import work, auth, work_comment, work_like, image_storage
import logging

@app.route('/work/<int:work_id>', methods = ['GET', 'POST'])
@auth.requires(auth.type.author)
def type_work(work_id) :
    session['work_id'] = work_id

    _work_ = work.get('id', work_id, 1)
    if _work_ is None : abort(404)

    return render_template('work.html', work = _work_)

@app.route('/work/<int:work_id>/like', methods = ['POST'])
@auth.requires(auth.type.author)
def like_work(work_id) :
    try :
        like_now   = work_like.toggle(liker_id = session['author_id'], work_id = work_id)
        like_count = len(work_like.get('work_id', work_id))
        return jsonify( success = True, count = like_count, like = like_now)
    except :
        return jsonify( success = False, action = 'alert', body = 'Like Action Failed' )