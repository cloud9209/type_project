from flask import Flask

# Flask Instance & Config
app = Flask('application')
import config
app.config.update(dict(
    DEBUG = True,
    ENABLE_FLASK_DEBUG_TB = True
))

# Jinja Extension
app.jinja_env.add_extension('jinja2.ext.do')

# [Flask Extension] SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# [Flask Extension] DebugToolbar
if app.config['ENABLE_FLASK_DEBUG_TB'] == True :
    from flask.ext.debugtoolbar import DebugToolbarExtension
    from application.models.image_storage import load_base64
    app.config['DEBUG_TB_PROFILER_ENABLED'] = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    toolbar = DebugToolbarExtension(app)
    app.jinja_env.globals.update(load_base64=load_base64)

# [Flask Extension] Signup with Google
from flask.ext.oauthlib.client import OAuth
oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key         = app.config.get('GOOGLE_CLIENT_ID'),
    consumer_secret      = app.config.get('GOOGLE_CLIENT_SECRET'),
    request_token_params = {
        'scope' : 'https://www.googleapis.com/auth/userinfo.email'
    },
    base_url             = 'https://www.googleapis.com/oauth2/v1/',
    request_token_url    =  None,
    access_token_method  = 'POST',
    access_token_url     = 'https://accounts.google.com/o/oauth2/token',
    authorize_url        = 'https://accounts.google.com/o/oauth2/auth',
)
facebook = oauth.remote_app(
    'facebook',
    consumer_key         = app.config.get('FACEBOOK_APP_ID'),
    consumer_secret      = app.config.get('FACEBOOK_APP_SECRET'),
    request_token_params = {
        'scope' : ['email', 'public_profile']
    },
    base_url             = 'https://graph.facebook.com',
    request_token_url    =  None,
    access_token_url     = '/oauth/access_token',
    authorize_url        = 'https://www.facebook.com/dialog/oauth',
)

# [Jinja] Unicode String Truncator : WILL CHANGE ALL WHITESPACE TO SPACE
import unicodedata
def u_width(u_str) :
    return sum( 1 + (unicodedata.east_asian_width(u_char) in "WF") for u_char in u_str )

@app.template_filter()
def u_truncate(u_str, max_width = app.config.get('STRING_TRUNCATE_LENGTH'), encoding = 'utf-8', ending = '...') :
    if u_width(u_str) < max_width : return u_str
    max_width -= len(ending)
    _unicode_, _width_ = u'', 0
    words = u_str.split()
    for word in words :
        _word_width_ = u_width(word)
        if _word_width_ + _width_ > max_width :
            return _unicode_ + ending
        _unicode_ += '%s ' % word
        _width_ += _word_width_ + 1
    return _unicode_

from datetime import datetime
@app.template_filter()
def pretty_date(dt, default = None):
    if default is None : default = 'just now'
    diff = datetime.utcnow() - dt
    periods = (
        (diff.days / 365    ,   'year',   'years'),
        (diff.days / 30     ,  'month',  'months'),
        (diff.days / 7      ,   'week',   'weeks'),
        (diff.days          ,    'day',    'days'),
        (diff.seconds / 3600,   'hour',   'hours'),
        (diff.seconds / 60  , 'minute', 'minutes'),
        (diff.seconds       , 'second', 'seconds'),
    )
    for period, singular, plural in periods :
        if not period : continue
        if period == 1: return u'%d %s ago' % (period, singular)
        else          : return u'%d %s ago' % (period, plural)
    return default

# Import Every function in 'controllers' directory
from application.models import schema
import os
for base, dirs, names in os.walk(os.path.join('application', 'controllers')):
    for name in filter(lambda s: s.endswith('.py') and s != '__init__.py', names) :
        exec('from application.controllers.'+name[:-3]+' import *')