from application import db
from schema import Author, TypeProjectComment
from flask import session, request
import datetime
from attrdict import attrdict
'''
class TypeProjectComment(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    body                = db.Column(db.Text())
    creation_time       = db.Column(db.DateTime, default=db.func.now())
    project_id          = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project             = db.relationship('TypeProject', foreign_keys = [project_id])
    writer_id           = db.Column(db.Integer, db.ForeignKey('author.id'))
    writer              = db.relationship('Author', foreign_keys = [writer_id])
    modified            = db.Column(db.Boolean, default = '0', onupdate = '1')
    modified_time       = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
'''

def add(writer_id, project_id, body) :
    _comment = TypeProjectComment (
        writer_id = writer_id,
        project_id = project_id,
        body = body
    )
    db.session.add( _comment )
    db.session.commit()
    return _comment

def modify(comment_id, body) :
    _comment = get('id', comment_id, 1)
    _comment.body = body
    db.session.commit()
    return _comment

def remove(comment_id) :
    _comment = get('id', comment_id, 1)
    db.session.delete(_comment)
    db.session.commit()
    return _comment

def get(attr = None, value = None, limit = -1) :
    project_comments = None
    if (attr, value) == (None, None) : project_comments = TypeProjectComment.query.filter()
    else                             : project_comments = TypeProjectComment.query.filter(getattr(TypeProjectComment, attr) == value)

    comments = []
    try :
        if   limit == 1 : comments =[project_comments.one()]
        elif limit >  1 : comments = project_comments.limit(limit)
        else            : comments = project_comments.all()
    except :
        return None

    for comment in comments :
        comment.creation_time += datetime.timedelta(hours=9)

    if limit == 1 : return comments[0]
    else          : return comments

def secure() :
    safe, action, body = None, None, None
    if 'project_id' not in session :
        safe = False
    elif 'comment_id' not in request.form :
        safe = False
        body = 'comment_id not exist'
    else :
        try :
            _comment = TypeProjectComment.query.filter(
                getattr(TypeProjectComment,         'id') == request.form['comment_id'],
                getattr(TypeProjectComment, 'project_id') == session['project_id'],
                getattr(TypeProjectComment,  'writer_id') == session['author_id'],
            ).one()
            safe = _comment is not None
        except :
            safe = False
            body = 'could not find proper project_comment object'
    return attrdict( safe = safe, action = action, body = body )