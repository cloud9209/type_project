from application import db
from schema import Author, TypeProjectComment
from flask import session, request
from attrdict import attrdict
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

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
    comment = TypeProjectComment (
        writer_id = writer_id,
        project_id = project_id,
        body = body
    )
    db.session.add( comment )
    db.session.commit()
    return comment

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
    project_comments = None
    if (attr, value) == (None, None) : project_comments = TypeProjectComment.query.filter()
    else                             : project_comments = TypeProjectComment.query.filter(getattr(TypeProjectComment, attr) == value)

    if limit == 1 :
        try    : return project_comments.one()
        except : return default
    elif limit > 1 : return project_comments.limit(limit)
    else           : return project_comments.all()

def secure() :
    safe, action, body = None, 'alert', None
    if 'project_id' not in session :
        safe = False
    elif 'comment_id' not in request.form :
        safe = False
        body = 'comment_id not exist'
    else :
        try :
            safe = TypeProjectComment.query.filter(
                getattr(TypeProjectComment,         'id') == request.form['comment_id'],
                getattr(TypeProjectComment, 'project_id') == session['project_id'],
                getattr(TypeProjectComment,  'writer_id') == session['user_id'],
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