from application import db
from schema import Author, TypeWorkLike
from flask import session
import datetime
from attrdict import attrdict

'''
class TypeWorkLike(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    work_id         = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    work            = db.relationship('TypeWork', foreign_keys = [work_id])
    liker_id        = db.Column(db.Integer, db.ForeignKey('author.id'))
    liker           = db.relationship('Author', foreign_keys = [liker_id])
'''
def add(writer_id, work_id) :
    db.session.add( TypeWorkLike (
        writer_id = writer_id,
        work_id = work_id
    ))
    db.session.commit()

def toggle(liker_id, project_id) :
    try :
        _like = TypeWorkLike.query.filter(
            TypeWorkLike.liker_id == liker_id,
            TypeWorkLike.project_id == project_id
        ).one()
        db.session.delete(_like)
        db.session.commit()
    except : # NoResult -> add, MultipleResult -> HAZARD!!
        add(liker_id, project_id)

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
    safe, action, body = None, None, None
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
                getattr(TypeWorkLike, 'writer_id' ) == session['author_id'],
            ).one()
            safe = _like is not None
        except :
            safe = False
            body = 'could not find proper work_like object'
    return attrdict( safe = safe, action = action, body = body )