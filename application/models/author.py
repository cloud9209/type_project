from application import db
from schema import Author
from flask import session
from attrdict import attrdict
import logging, auth

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

def verified(form) : 
    return Author.query.filter(
        Author.email    == form['email'],
        Author.password == db.func.md5(form['password'])
    ).count() != 0

def secure() :
    safe, action, body = None, None, None
    safe = 'author_id' in session and 'author_email' in session and 'author_name' in session and 'author_thumbnail' in session
    action = 'abort'
    return attrdict( safe = safe, action = action, body = body )