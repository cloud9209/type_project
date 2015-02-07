from application import app
from flask import url_for, request, session, redirect

# Set Default Configurations
app.config.update(dict(
    STRING_TRUNCATE_LENGTH = 115,
    ENABLE_FLASK_DEBUG_TB = False,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI ='mysql+gaerdbms:///type_db?instance=cloud-9209:typedesign-instance',
    migration_directory = 'migrations'
))