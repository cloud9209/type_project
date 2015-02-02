from attrdict import attrdict
from application import db
from flask import session
from schema import Author

def verified(form) : 
    return Author.query.filter(
        Author.email    == form['email'],
        Author.password == db.func.md5(form['password'])
    ).count() != 0

def secure() :
    safe, action, body = None, None, None
    safe = 'user_id' in session and 'user_email' in session and 'user_name' in session and 'user_thumbnail' in session
    action = 'abort'
    return attrdict( safe = safe, action = action, body = body )