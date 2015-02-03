# Flask Instance
from flask import Flask
app = Flask('application')
import config

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
from flask.ext.debugtoolbar import DebugToolbarExtension
from application.models.image_storage import load_base64
import logging
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)
app.jinja_env.globals.update(load_base64=load_base64)
def unicode_truncate(_string_, length, encoding='utf-8'):
    logging.info('TRUNCATE')
    logging.warning(_string_)
    logging.warning(_string_.split())
    logging.info('--------')
    _str_encoded_ = _string_.encode(encoding)[:length - 4]
    return _str_encoded_.decode(encoding, 'ignore') + ' ...'

# http://stackoverflow.com/questions/13665001/python-truncating-international-string
# LENGTH_BY_PREFIX = [(0xC0, 2), (0xE0, 3), (0xF0, 4), (0xF8, 5), (0xFC, 6)] # first byte mask, total codepoint length

# def codepoint_length(first_byte):
#     if first_byte < 128:
#         return 1 # ASCII
#     for mask, length in LENGTH_BY_PREFIX:
#         if first_byte & mask == mask:
#             return length
#     assert False, 'Invalid byte %r' % first_byte

# def cut_to_bytes_length(unicode_text, byte_limit):
#     utf8_bytes = unicode_text.encode('UTF-8')
#     cut_index = 0
#     logging.info(['%02x' ])
#     while cut_index < len(utf8_bytes):
#         step = codepoint_length(ord(utf8_bytes[cut_index]))
#         if cut_index + step > byte_limit:
#             # can't go a whole codepoint further, time to cut
#             return utf8_bytes[:cut_index]
#         else:
#             cut_index += step
#     # length limit is longer than our bytes strung, so no cutting
#     return utf8_bytes
app.jinja_env.globals.update(truncate_u = unicode_truncate)#cut_to_bytes_length)
# Import Every function in 'controllers' directory
from application.models import schema
import os
for base, dirs, names in os.walk(os.path.join('application', 'controllers')):
    for name in filter(lambda s: s.endswith('.py') and s != '__init__.py', names) :
        exec('from application.controllers.'+name[:-3]+' import *')