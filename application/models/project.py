from application import db
from schema import Author, TypeProject
from flask import session
from attrdict import attrdict

def add(data) :
    db.session.add( TypeProject (
        category    = data['category'],
        title       = data['project_title'],
        description = data['description'],
        author_id   = session['author_id']
    ))
    db.session.commit()

def get(attr = None, value = None, limit = -1, default = None) :
    projects = None
    if (attr, value) == (None, None) : projects = TypeProject.query.filter()
    else                             : projects = TypeProject.query.filter(getattr(TypeProject, attr) == value)

    if limit == 1 :
        try    : return projects.one()
        except : return default
    elif limit > 1 : return projects.limit(limit)
    else           : return projects.all()

def remove(attr, value) :
    try :
        _target = TypeProject.query.filter(getattr(TypeProject, attr) == value).one()
    except :
        return False
    db.session.delete(_target)
    db.session.commit()
    return True

def secure() :
    safe, action, body = None, 'abort', None
    if 'project_id' not in session :
        safe = False
    else :
        try :
            _project = TypeProject.query.filter(
                getattr(TypeProject, 'author_id') == session['author_id'],
                getattr(TypeProject,        'id') == session['project_id']
            ).one()
            safe = _project is not None
        except :
            safe = False
            body = 'could not fine proper project obj'
    return attrdict( safe = safe, action = action, body = body )