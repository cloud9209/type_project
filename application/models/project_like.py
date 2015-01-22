from application import db
from schema import Author, TypeProjectLike
from flask import session
import datetime

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
    like_count = TypeProjectLike.query.filter(
        TypeProjectLike.liker_id == liker_id,
        TypeProjectLike.project_id == project_id
    ).count()

    if like_count :
        TypeProjectLike.query.filter(
            TypeProjectLike.liker_id == liker_id,
            TypeProjectLike.project_id == project_id
        ).delete()
    else :
        add(liker_id, project_id)

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