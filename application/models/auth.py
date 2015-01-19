from flask import session, abort
from functools import wraps

def secure():
    return 'id' in session and 'email' in session and 'name' in session

""" << Decorator Checking Authentication >> 
    : proceed if authorized
    : raise 404 page if not authorized  """
def required(f):
    @wraps(f)
    def deco(*args, **kwargs) :
        if not secure() : abort(404)
        return f(*args, **kwargs)
    return deco
