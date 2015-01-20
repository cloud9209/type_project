from application import db
from schema import Author, TypeProjectComment
from flask import session
import datetime
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
    db.session.add( TypeProjectComment (
        writer_id = writer_id,
        project_id = project_id,
        body = body
    ))
    db.session.commit()

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