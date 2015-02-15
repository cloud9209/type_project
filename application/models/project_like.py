from application import db
from schema import Author, TypeProjectLike
from flask import session, request
from attrdict import attrdict
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

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
    _is_liking_ = False
    try :
        _like_ = TypeProjectLike.query.filter(
            getattr(TypeProjectLike, 'liker_id') == liker_id,
            getattr(TypeProjectLike, 'project_id') == project_id
        ).one()
        db.session.delete(_like_)
    except NoResultFound :
        db.session.add( TypeProjectLike (
            liker_id = liker_id,
            project_id = project_id
        ))
        _is_liking_ = True
    except MultipleResultsFound :
        _likes_ = TypeProjectLike.query.filter(
            getattr(TypeProjectLike, 'liker_id') == liker_id,
            getattr(TypeProjectLike, 'project_id') == project_id
        ).all()
        for _like_ in _likes_ : db.session.delete(_like_)
    except :
        raise
    db.session.commit()
    return _is_liking_

def get(attr = None, value = None, limit = -1, default = None) :
    project_likes = None
    if (attr, value) == (None, None) : project_likes = TypeProjectLike.query.filter()
    else                             : project_likes = TypeProjectLike.query.filter(getattr(TypeProjectLike, attr) == value)

    if limit == 1 :
        try    : return project_likes.one()
        except : return default
    elif limit > 1 : return project_likes.limit(limit)
    else           : return project_likes.all()

def secure() :
    return attrdict( safe = False, action = 'alert', body = 'Authentication Function Not Implemented')
    # safe, action, body = None, 'alert', None
    # if 'project_id' not in session :
    #     safe = False
    # elif 'like_id' not in request.form :
    #     safe = False
    #     body = 'like_id not exist'
    # else :
    #     try :
    #         _like = TypeProjectComment.query.filter(
    #             getattr(TypeProjectComment,         'id') == request.form['like_id'],
    #             getattr(TypeProjectComment, 'project_id') == session['project_id'],
    #             getattr(TypeProjectComment,  'writer_id') == session['user_id']
    #         ).one()
    #         safe = _like is not None
    #     except :
    #         safe = False
    #         body = 'could not find proper project_like object'
    # return attrdict( safe = safe, action = action, body = body )