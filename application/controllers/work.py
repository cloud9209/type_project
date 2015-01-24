#_*_ coding:utf_8 _*_
from application import app
from flask import render_template, session, url_for, request, redirect, abort
from application.models import work, auth, work_comment
import logging

@app.route('/work/<int:work_id>', methods = ['GET', 'POST'])
@auth.requires(auth.type.author)
def type_work(work_id) :
    session['work_id'] = work_id

    __work__ = work.get('id', work_id, 1)
    if __work__ is None : abort(404)

    return render_template('work.html', work = __work__)