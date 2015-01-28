from application import db
from schema import Author, TypeWorkLike
from flask import session, request
import datetime
from attrdict import attrdict
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

'''
class TypeWorkLike(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    work_id         = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    work            = db.relationship('TypeWork', foreign_keys = [work_id])
    liker_id        = db.Column(db.Integer, db.ForeignKey('author.id'))
    liker           = db.relationship('Author', foreign_keys = [liker_id])
'''
def add(liker_id, work_id) :
    db.session.add( TypeWorkLike (
        liker_id = liker_id,
        work_id = work_id
    ))
    db.session.commit()

def toggle(liker_id, work_id) :
    try :
        _like_ = TypeWorkLike.query.filter(
            getattr(TypeWorkLike, 'liker_id') == liker_id,
            getattr(TypeWorkLike, 'work_id') == work_id
        ).one()
        db.session.delete(_like_)
    except NoResultFound :
        db.session.add(TypeWorkLike(
            liker_id = liker_id,
            work_id = work_id
        ))
    except MultipleResultsFound :
        _likes_ = TypeWorkLike.query.filter(
            getattr(TypeWorkLike, 'liker_id') == liker_id,
            getattr(TypeWorkLike, 'work_id') == work_id
        ).all()
        for _like_ in _likes_ : db.session.delete(_like_)
    except :
        raise
    db.session.commit()
    return len(get('work_id', work_id))
    
def get(attr = None, value = None, limit = -1) :
    work_likes = None
    if (attr, value) == (None, None) : work_likes = TypeWorkLike.query.filter()
    else                             : work_likes = TypeWorkLike.query.filter(getattr(TypeWorkLike, attr) == value)

    likes = []
    try :
        if   limit == 1 : likes =[work_likes.one()]
        elif limit >  1 : likes = work_likes.limit(limit)
        else            : likes = work_likes.all()
    except :
        return None

    if limit == 1 : return likes[0]
    else          : return likes

def secure() :
    safe, action, body = None, 'alert', None
    if 'work_id' not in session :
        safe = False
    elif 'like_id' not in request.form :
        safe = False
        body = 'like_id not exist'
    else :
        try :
            _like = TypeWorkLike.query.filter(
                getattr(TypeWorkLike, 'id'        ) == request.form['like_id'],
                getattr(TypeWorkLike, 'work_id') == session['work_id'],
                getattr(TypeWorkLike, 'liker_id' ) == session['author_id'],
            ).one()
            safe = _like is not None
        except :
            safe = False
            body = 'could not find proper work_like object'
    return attrdict( safe = safe, action = action, body = body )