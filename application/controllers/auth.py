# -*- coding: utf-8 -*-
from application import app, google, facebook
from flask import render_template, session, url_for, request, redirect, jsonify
from application.models import author, signin
import logging

# Normal Sign in/up
@app.route('/sign_in', methods=['POST'])
def sign_in() :
    _author_ = signin.get_verified_user(request.form)
    if _author_ is None : return jsonify( success = False, action = 'alert', body = 'SignIn Failure' )
    
    session['user_id'       ] = _author_.id
    session['user_name'     ] = _author_.name
    session['user_email'    ] = _author_.email
    session['user_thumbnail'] = _author_.thumbnail
    next_url = request.referrer
    if next_url is None : raise # Initial Setting to Catch a BUG
    return jsonify( success = True, action = 'redirect', body = next_url)

@app.route('/sign_up', methods=['POST'])
def sign_up() :
    success = author.add_exclusively(request.form)
    if not success : return jsonify( success = False, action = 'alert', body = 'SignUp Failure : E-mail Duplication' )
    else           : return jsonify( success =  True, action = 'alert', body = 'SignUp Success' )

@app.route('/sign_out')
def sign_out() :
    session.clear() # includes session.pop('google_token', None)
    return redirect(url_for('index'))

# Google Sign in/up
'''{ <google oauth2 response data format>
  "data": {
    "email": "pjhjohn@gmail.com", 
    "family_name": "\ubc15", 
    "gender": "male", 
    "given_name": "\uc900\ud638", 
    "id": "109531791275452303304", 
    "link": "https://plus.google.com/109531791275452303304", 
    "name": "\ubc15\uc900\ud638", 
    "picture": "https://lh6.googleusercontent.com/-aztZgiirtTg/AAAAAAAAAAI/AAAAAAAABIQ/VSlhPhUIogE/photo.jpg", 
    "verified_email": true
  }
}'''
@app.route('/oauth/google')
def oauth_google() :
    if request.referrer :
        session['next_url'] = request.referrer
    return google.authorize(callback = url_for('oauth_google_authorized', _external = True))

@app.route('/oauth/google/authorized')
def oauth_google_authorized() :
    resp = google.authorized_response()

    # Not Authorized
    if resp is None :
        return 'Access Denied : reason = %s, error = %s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    # Authorized
    try :
        session['google_token'] = (resp['access_token'], '')
    except TypeError :
        abort(404) # TODO : Better Handling

    # user_info availiable
    user_info = google.get('userinfo').data
    _author_ = author.get('email', user_info['email'], 1)
    
    # Register If Not Exist
    success = author.add_exclusively(user_info, 'GOOGLE')
    if not success : return 'Registration Failed'

    _author_ = author.get('email', user_info['email'], 1)
    logging.critical('compare : %s, %s' %(_author_.googleplus_id, user_info['id']))
    if _author_.googleplus_id == user_info['id'] :
        session['user_id'       ] = _author_.id
        session['user_name'     ] = _author_.name
        session['user_email'    ] = _author_.email
        session['user_thumbnail'] = _author_.thumbnail
        next_url = session.pop('next_url', None)
        logging.critical('next : ' + str(next_url))
        logging.critical('redirect target : ' + str(next_url or url_for('main')))
        return redirect(next_url or url_for('main'))
    logging.critical('Authentication Fail for %s : [%s] != [%s]' % (user_info['email'], _author_.googleplus_id, user_info['id']))
    return 'Login Failed.'

@google.tokengetter
def get_google_oauth_token() :
    return session.get('google_token')



# Facebook Sign in/up
'''{ <facebook oauth response data format>
  "email": "pjhjohn@gmail.com", 
  "first_name": "Joon Ho", 
  "gender": "male", 
  "id": "864299036962877", 
  "last_name": "Park", 
  "link": "https://www.facebook.com/app_scoped_user_id/864299036962877/", 
  "locale": "ko_KR", 
  "name": "Joon Ho Park", 
  "timezone": 9, 
  "updated_time": "2015-02-11T11:49:24+0000", 
  "verified": true
}'''
@app.route('/oauth/facebook')
def oauth_facebook() :
    if request.referrer :
        session['next_url'] = request.referrer
    return facebook.authorize(callback = url_for('oauth_facebook_authorized', _external = True))

@app.route('/oauth/facebook/authorized')
def oauth_facebook_authorized() :
    resp = facebook.authorized_response()

    # Not Authorized
    if resp is None :
        return 'Access Denied : reason = %s, error = %s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    # Authorized
    try :
        session['facebook_token'] = (resp['access_token'], '')
    except TypeError :
        abort(404) # TODO : Better Handling

    # user_info availiable
    user_info = facebook.get('/me').data
    _author_ = author.get('email', user_info['email'], 1)

    # Register If Not Exist
    success = author.add_exclusively(user_info, 'FACEBOOK')
    if not success : return 'Registration Failed'

    _author_ = author.get('email', user_info['email'], 1)
    logging.critical('compare : %s, %s' %(_author_.facebook_id, user_info['id']))
    if _author_.facebook_id == user_info['id'] :
        session['user_id'       ] = _author_.id
        session['user_name'     ] = _author_.name
        session['user_email'    ] = _author_.email
        session['user_thumbnail'] = _author_.thumbnail
        next_url = session.pop('next_url', None)
        logging.critical('next : ' + str(next_url))
        logging.critical('redirect target : ' + str(next_url or url_for('main')))
        return redirect(next_url or url_for('main'))
    logging.critical('Authentication Fail for %s : [%s] != [%s]' % (user_info['email'], _author_.facebook_id, user_info['id']))
    return 'Login Failed.'        

@facebook.tokengetter
def get_facebook_oauth_token() :
    return session.get('facebook_token')

