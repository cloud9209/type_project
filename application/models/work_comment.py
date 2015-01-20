from application import db
from schema import Author, TypeWorkComment
from flask import session

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

    if limit == 1 :
        try :
            return work_comments.one()
        except :
            return None
    elif  limit >  1 : return work_comments.limit(limit)
    else             : return work_comments.all()