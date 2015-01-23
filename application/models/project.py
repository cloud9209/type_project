from application import db
from schema import Author, TypeProject
from flask import session

def add(data) :
    db.session.add( TypeProject (
        category    = data['category'],
        title       = data['project_title'],
        description = data['description'],
        author_id   = session['author_id']
    ))
    db.session.commit()

def get(attr = None, value = None, limit = -1, with_author = False, default = None) :
    projects = None
    if with_author : 
        if (attr, value) == (None, None) : projects = TypeProject.query.filter(getattr(TypeProject, 'author_id') == session['author_id'])
        else                             : projects = TypeProject.query.filter(getattr(TypeProject, 'author_id') == session['author_id'], getattr(TypeProject, attr) == value)
    else :
        if (attr, value) == (None, None) : projects = TypeProject.query.filter()
        else                             : projects = TypeProject.query.filter(getattr(TypeProject, attr) == value)

    if limit == 1 :
        try :
            return projects.one()
        except :
            return default
            
    elif  limit >  1 : return projects.limit(limit)
    else             : return projects.all()

def remove(attr, value) :
    try :
        _target = TypeProject.query.filter(getattr(TypeProject, attr) == value).one()
    except :
        return False
    db.session.delete(_target)
    db.session.commit()
    return True