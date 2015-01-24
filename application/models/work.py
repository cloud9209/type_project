from application import db
from schema import TypeWork
from flask import session
import datetime
from attrdict import attrdict

'''
class TypeWork(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    image               = db.Column(db.String(100))
    description         = db.Column(db.Text())
    date                = db.Column(db.DateTime, default=db.func.now())
    project_id          = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project             = db.relationship('TypeProject', foreign_keys = [project_id])
    comments            = db.relationship('TypeWorkComment', backref='type_work', lazy='dynamic')
'''
def add(data) :
    db.session.add(TypeWork(
        description = data['description'],
        project_id = session['project_id']
    ))
    db.session.commit()

def add_project_copy(prj) :
    db.session.add(TypeWork(
        description = prj.description,
        project_id = prj.id,
        image = prj.thumbnail
    ))
    db.session.commit()

def get(attr = None, value = None, limit = -1, default = None) :
    type_works = None
    
    if (attr, value) == (None, None) : type_works = TypeWork.query.filter()
    else                             : type_works = TypeWork.query.filter(getattr(TypeWork, attr) == value)

    works = []
    try :
        if limit == 1 : works =[type_works.one()]
        if limit >  1 : works = type_works.limit(limit)
        else          : works = type_works.all()
    except :
        return default

    for work in works :
        work.date += datetime.timedelta(hours=9)

    if limit == 1 : return works[0]
    else          : return works

def remove(attr, value) :
    try :
        _target = TypeWork.query.filter(getattr(TypeWork, attr) == value).one()
    except :
        return False
    db.session.delete(_target)
    db.session.commit()
    return True

def secure() :
    safe, action, body = None, 'abort', None
    if 'work_id' not in session :
        safe = False
    else :
        try :
            _work = TypeWork.query.filter(
                getattr(TypeWork, 'author_id') == session['author_id'],
                getattr(TypeWork,        'id') == session['work_id']
            ).one()
            safe = _work is not None
        except :
            safe = False
            body = 'could not find proper work obj'
    return attrdict( safe = safe, action = action, body = body )
