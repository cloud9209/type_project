from flask import session, abort, request, jsonify
from functools import wraps
import author, project, project_comment, project_like, work, work_comment, work_like
import logging, sys

""" enum declaration """
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

""" type of authentication : will override type keyword from here. """
type = enum('author', 'project', 'project_comment', 'project_like', 'work', 'work_comment', 'work_like')
def secure(auth_type) :
    response = None
    target = type.reverse_mapping[auth_type] + ".secure()"
    logging.debug(target)
    try :
        response = eval( target )
    except SyntaxError :
        logging.debug("Tried to call " + target + ", failed with SyntaxError. ")
        raise
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
            if response is None : return jsonify(success = False, action = 'alert', body = "SyntaxError While exec")

            # Successfully received response via eval
            if response.safe :
                logging.info('entering ' + _function_.__name__)
                return _function_(*args, **kwargs)
            elif response.action == 'abort' :
                abort(404)
            elif response.action == 'alert' :
                return jsonify(success = False, action = 'alert', body = response.body)
            else :
                return jsonify(success = False, body = response.body)
        return argument_wrapper
    return function_wrapper