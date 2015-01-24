from application import db
from schema import Author, TypeWorkComment
from flask import session
import datetime
from attrdict import attrdict

'''
class TypeWorkComment(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    body            = db.Column(db.Text())
    creation_time   = db.Column(db.DateTime, default = db.func.now())
    work_id         = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    work            = db.relationship('TypeWork', foreign_keys = [work_id])
    writer_id       = db.Column(db.Integer, db.ForeignKey('author.id'))
    writer          = db.relationship('Author', foreign_keys = [writer_id])
    modified        = db.Column(db.Boolean, default = '0', onupdate = '1')
    modified_time   = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
'''

def add(writer_id, work_id, body) :
    db.session.add( TypeWorkComment (
        writer_id = writer_id,
        work_id = work_id,
        body = body
    ))
    db.session.commit()

def get(attr = None, value = None, limit = -1) :
    work_comments = None
    if (attr, value) == (None, None) : work_comments = TypeWorkComment.query.filter()
    else                             : work_comments = TypeWorkComment.query.filter(getattr(TypeWorkComment, attr) == value)

    comments = []
    try :
        if   limit == 1 : comments =[work_comments.one()]
        elif limit >  1 : comments = work_comments.limit(limit)
        else            : comments = work_comments.all()
    except :
        return None

    for comment in comments :
        comment.creation_time += datetime.timedelta(hours=9)

    if limit == 1 : return comments[0]
    else          : return comments

def secure() :
    safe, action, body = None, None, None
    if 'work_id' not in session :
        safe = False
    elif 'comment_id' not in request.form :
        safe = False
        body = 'comment_id not exist'
    else :
        try :
            _comment = TypeWorkComment.query.filter(
                getattr(TypeWorkComment, 'id'        ) == request.form['comment_id'],
                getattr(TypeWorkComment, 'work_id') == session['work_id'],
                getattr(TypeWorkComment, 'writer_id' ) == session['author_id'],
            ).one()
            safe = _comment is not None
        except :
            safe = False
            body = 'could not find proper work_comment object'
    return attrdict( safe = safe, action = action, body = body )