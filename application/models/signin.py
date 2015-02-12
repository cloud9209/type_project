from attrdict import attrdict
from application import db
from flask import session
from schema import Author
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import logging
def get_verified_user(form) : 
    author = None
    try :
        author = Author.query.filter(
            Author.email    == form['email'],
            Author.password == db.func.md5(form['password'])
        ).one()
    except NoResultFound :
        pass
    except MultipleResultsFound :
        logging.critical("Multiple User has same ID & PASSWD")
        raise
    except :
        logging.critical("Unextected Error")
        raise
    return author        

def secure() :
    safe, action, body = None, None, None
    safe = 'user_id' in session and 'user_email' in session and 'user_name' in session and 'user_thumbnail' in session
    action = 'abort'
    return attrdict( safe = safe, action = action, body = body )