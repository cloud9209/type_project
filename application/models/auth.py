from flask import session, abort, request, jsonify
from functools import wraps
from application.models import project, work
import logging, sys

""" attrdict """
class attrdict(dict):
    def __init__(self, *args, **kwargs) :
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self
    def retrieve(self, key, value) :
        if key in self :
            return self[key]
        else :
            self[key] = value
            return value

""" enum """
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

""" checking functions for various type of secure """
def secure_signed_in() :
    logging.debug('secure_signed_in')
    return attrdict(
        safe = 'author_id' in session and 'author_email' in session and 'author_name' in session,
        action = 'abort'
    )

def secure_project() :
    safe, action, body = None, None, None
    if 'project_id' not in session :
        safe = False
    else :
        _project = project.get('id', session['project_id'], 1, True)
        safe = _project is not None
    return attrdict( safe = safe, action = action, body = body )

def secure_work() :
    safe, action, body = None, None, None
    if 'work_id' not in session :
        safe = False
    else :
        _work = work.get('id', session['work_id'], 1, True)
        safe = _work is not None
    return attrdict( safe = safe, action = action, body = body )

""" type of authentication : will override type keyword from here. """
type = enum('signed_in', 'project', 'project_comment', 'project_like', 'work', 'work_comment', 'work_like')
def secure(auth_type) :
    response = None
    target = "secure_" + type.reverse_mapping[auth_type]
    logging.debug(target)
    try :
        response = eval( target + '()' )
        logging.debug('safe exit')
    except SyntaxError :
        logging.debug("Tried to call " + target + ", failed with SyntaxError. ")
    except :
        logging.debug ("Unexpected error:", sys.exc_info()[0])
        raise
    return response
""" Universal Authentication Handler : Uses Function Above via <eval> """
def requires(auth_type) :
    def function_wrapper(_function_) :
        @wraps(_function_)
        def argument_wrapper(*args, **kwargs) :
            response = secure(auth_type)
            logging.info(response)
            # SyntaxError : response == None
            if response is None : return jsonify(success = False, message = "SyntaxError While exec")

            # Successfully received response via eval
            if response.safe :
                return _function_(*args, **kwargs)
            elif response.action == 'abort' :
                abort(404)
            else :
                return jsonify(success = False, message = response.body)
        return argument_wrapper
    return function_wrapper

""" << Decorator Checking Authentication >> 
    : proceed if authorized
    : raise 404 page if not authorized  """
# def required(f):
#     @wraps(f)
#     def auth_required(*args, **kwargs) :
#         if secure() : return f(*args, **kwargs)
#         # Not Secure
#         if   request.method == 'POST' : return jsonify(success = False)
#         elif request.method == 'GET'  : abort(404)
#         else :
#             logging.debug("Invlid request method : " + str(request.method))
#             abort(404)
#     return auth_required

# def project_owner_only(f) :
#     @wraps(f)
#     def auth_project_owner_only(*args, **kwargs) :
#         if secure() and secure_project() : return f(*args, **kwargs)

#         if request.method == 'POST' : return jsonify(success = False)
#         else : 
#             logging.debug(f.__name__ + " only takes POST Request.")
#             abort(404)
#     return auth_project_owner_only

# def work_owner_only(f) :
#     @wraps(f)
#     def auth_work_owner_only(*args, **kwargs) :
#         if secure() and secure_work() : return f(*args, **kwargs)

#         if request.method == 'POST' : return jsonify(success = False)
#         else : 
#             logging.debug(f.__name__ + " only takes POST Request.")
#             abort(404)
#     return auth_work_owner_only
