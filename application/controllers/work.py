#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import work, auth, work_comment
import logging

@app.route('/work/<int:work_id>', methods = ['GET', 'POST'])
@auth.required # 404 if not authorized
def type_work(work_id) :
    session['work-id'] = work_id

    current_work = work.get('id', work_id, 1)
    if current_work is None : abort(404)

    return render_template('work.html', work = current_work,
        likes    = [],#   work_like.get('work_id', work_id),
        comments = work_comment.get('work_id', work_id)
    )