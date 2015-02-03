from application import db
from schema import Author
from flask import session, request
from attrdict import attrdict

def add(data) :
    db.session.add( Author (
        email = data['email'],
        password = db.func.md5(data['password']),
        name = data['name']
    ))
    db.session.commit()

def add_exclusive(data) :
    if len(get('email', data['email'])) : return False    
    add(data)
    return True

def get (attr = None, value = None, limit = -1) :
    authors = None
    if (attr, value) == (None, None) : authors = Author.query.filter()
    else                             : authors = Author.query.filter(getattr(Author, attr) == value)

    if limit == 1 :
        try    : return authors.one()
        except : return None        
    elif limit >  1 : return authors.limit(limit)
    else            : return authors.all()

def secure() :
    safe, action, body = None, ['alert', 'abort'][request.method=='GET'], None
    if 'author_id' not in session :
        safe = False
        body = 'Not Authorized : Invalid Access Sequence'
    else :
        if session['author_id'] == session['user_id'] :
            safe = True
        else :
            safe = False
            body = 'Not Authorized'
    return attrdict( safe = safe, action = action, body = body )
