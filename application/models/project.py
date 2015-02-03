from application import db
from schema import Author, TypeProject
from flask import session, request
from attrdict import attrdict
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

def add(data) :
    db.session.add( TypeProject (
        category    = data['category'],
        title       = data['project_title'],
        description = data['description'],
        author_id   = session['user_id']
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

def set(id, attr, value) :
    _project = None
    try :
        _project = get('id', id, 1)
        setattr(_project, attr, value)
        db.session.commit()
    except NoResultFound :
        raise
    except MultipleResultsFound :
        raise
    except :
        raise
    return _project

def remove(attr, value) :
    try :
        _target = TypeProject.query.filter(getattr(TypeProject, attr) == value).one()
    except :
        return False
    db.session.delete(_target)
    db.session.commit()
    return True

def secure() :
    safe, action, body = None, ['alert', 'abort'][request.method=='GET'], None
    if 'project_id' not in session :
        safe = False
    else :
        try :
            _project = TypeProject.query.filter(
                getattr(TypeProject, 'author_id') == session['user_id'],
                getattr(TypeProject,        'id') == session['project_id']
            ).one()
            safe = _project is not None
        except NoResultFound :
            safe = False
            body = 'Not Authorized'
        except MultipleResultsFound :
            safe = False
            body = 'DB Error : Multiple Result Found'
        except :
            safe = False
            body = 'Unexpected Error'
    return attrdict( safe = safe, action = action, body = body )
