from application import db
from schema import Author, TypeWorkComment
from flask import session, request
from attrdict import attrdict
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

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
    _work = TypeWorkComment (
        writer_id = writer_id,
        work_id = work_id,
        body = body
    )
    db.session.add( _work )
    db.session.commit()
    return _work

def modify(comment_id, body) :
    comment = get('id', comment_id, 1)
    comment.body = body
    db.session.commit()
    return comment

def remove(comment_id) :
    comment = get('id', comment_id, 1)
    db.session.delete(comment)
    db.session.commit()
    return comment

def get(attr = None, value = None, limit = -1, default = None) :
    work_comments = None
    if (attr, value) == (None, None) : work_comments = TypeWorkComment.query.filter()
    else                             : work_comments = TypeWorkComment.query.filter(getattr(TypeWorkComment, attr) == value)
    
    if limit == 1 :
        try    : return work_comments.one()
        except : return default
    elif limit > 1 : return work_comments.limit(limit)
    else           : return work_comments.all()

def secure() :
    safe, action, body = None, 'alert', None
    if 'work_id' not in session :
        safe = False
    elif 'comment_id' not in request.form :
        safe = False
        body = 'comment_id not exist'
    else :
        try :
            safe = TypeWorkComment.query.filter(
                getattr(TypeWorkComment,        'id' ) == request.form['comment_id'],
                getattr(TypeWorkComment,   'work_id' ) == session['work_id'],
                getattr(TypeWorkComment, 'writer_id' ) == session['user_id'],
            ).one() is not None
        except NoResultFound :
            safe = False
            body = 'Not Authorized'
        except MultipleResultsFound :
            safe = False
            body = 'DB Error : Multiple Result Found'
        except :
            safe = False
            body = 'Unexpected Error'
    return attrdict( safe = safe, action = action, body = body )