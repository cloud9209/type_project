from flask import session, abort, request, jsonify
from functools import wraps
from application.models import project, work
import logging

def secure():
    return 'author_id' in session and 'author_email' in session and 'author_name' in session

def secure_project() :
    if 'project_id' not in session : return False
    _project = project.get('project_id', session['project_id'], with_author = True)
    return _project is not None

def secure_work() :
    if 'work_id' not in session : return False
    _work = work.get('work_id', session['work_id'], with_author = True)
    return _work is not None

""" << Decorator Checking Authentication >> 
    : proceed if authorized
    : raise 404 page if not authorized  """
def required(f):
    @wraps(f)
    def auth_required(*args, **kwargs) :
        if secure() : return f(*args, **kwargs)
        # Not Secure
        if   request.method == 'POST' : return jsonify(success = False)
        elif request.method == 'GET'  : abort(404)
        else :
            logging.debug("Invlid request method : " + str(request.method))
            abort(404)
    return auth_required

def project_owner_only(f) :
    @wraps(f)
    def auth_project_owner_only(*args, **kwargs) :
        if secure() and secure_project() : return f(*args, **kwargs)

        if request.method == 'POST' : return jsonify(success = False)
        else : 
            logging.debug(f.__name__ + " only takes POST Request.")
            abort(404)
    return auth_project_owner_only

def work_owner_only(f) :
    @wraps(f)
    def auth_work_owner_only(*args, **kwargs) :
        if secure() and secure_work() : return f(*args, **kwargs)

        if request.method == 'POST' : return jsonify(success = False)
        else : 
            logging.debug(f.__name__ + " only takes POST Request.")
            abort(404)
    return auth_work_owner_only