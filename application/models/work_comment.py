from application import db
from schema import Author, TypeWorkComment
from flask import session
import datetime

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