from flask import session, abort, request
from functools import wraps
import logging

def secure():
    return 'id' in session and 'email' in session and 'name' in session

""" << Decorator Checking Authentication >> 
    : proceed if authorized
    : raise 404 page if not authorized  """
def required(f):
    @wraps(f)
    def auth_required(*args, **kwargs) :
        if not secure() :
            if request.method == 'POST' :
                return '1'
            elif request.method == 'GET' :
                abort(404)
            else :
                abort(404)
        return f(*args, **kwargs)
    return auth_required
