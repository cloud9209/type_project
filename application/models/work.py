from application import db
from schema import TypeWork
from flask import session

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
        project_id = session['project-id']
    ))
    db.session.commit()

def add_project_copy(prj) :
    db.session.add(TypeWork(
        description = prj.description,
        project_id = prj.id,
        image = prj.thumbnail
    ))
    db.session.commit()

def to_date(date) :
    return date # to date in yyyy mm dd hh mm

def get(attr = None, value = None, limit = -1) :
    works = None
    if (attr, value) == (None, None) : works = TypeWork.query.filter()
    else                             : works = TypeWork.query.filter(getattr(TypeWork, attr) == value)

    if limit == 1 :
        try :
            return works.one()
        except :
            return None
    if  limit >  1 : return works.limit(limit)
    else           : return works.all()