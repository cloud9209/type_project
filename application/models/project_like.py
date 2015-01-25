from application import db
from schema import Author, TypeProjectLike
from flask import session, request
import datetime
from attrdict import attrdict

'''
class TypeProjectLike(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    project_id      = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project         = db.relationship('TypeProject', foreign_keys = [project_id])
    liker_id        = db.Column(db.Integer, db.ForeignKey('author.id'))
    liker           = db.relationship('Author', foreign_keys = [liker_id])
'''

def add(liker_id, project_id) :
    db.session.add( TypeProjectLike (
        liker_id = liker_id,
        project_id = project_id
    ))
    db.session.commit()

# IS THERE ANY TIMING ISSUE ON THIS???
def toggle(liker_id, project_id) :
    try :
        _like = TypeProjectLike.query.filter(
            getattr(TypeProjectLike, 'liker_id') == liker_id,
            getattr(TypeProjectLike, 'project_id') == project_id
        ).first()
        if _like is None :
            add(liker_id, project_id)
        else :
            db.session.delete(_like)
            db.session.commit()
    except :
        raise

    return len(get('project_id', project_id))

def get(attr = None, value = None, limit = -1) :
    project_likes = None
    if (attr, value) == (None, None) : project_likes = TypeProjectLike.query.filter()
    else                             : project_likes = TypeProjectLike.query.filter(getattr(TypeProjectLike, attr) == value)

    likes = []
    try :
        if   limit == 1 : likes =[project_likes.one()]
        elif limit >  1 : likes = project_likes.limit(limit)
        else            : likes = project_likes.all()
    except :
        return None

    if limit == 1 : return likes[0]
    else          : return likes

def secure() :
    safe, action, body = None, None, None
    if 'project_id' not in session :
        safe = False
    elif 'like_id' not in request.form :
        safe = False
        body = 'like_id not exist'
    else :
        try :
            _like = TypeProjectComment.query.filter(
                getattr(TypeProjectComment,         'id') == request.form['like_id'],
                getattr(TypeProjectComment, 'project_id') == session['project_id'],
                getattr(TypeProjectComment,  'writer_id') == session['author_id']
            ).one()
            safe = _like is not None
        except :
            safe = False
            body = 'could not find proper project_like object'
    return attrdict( safe = safe, action = action, body = body )