from application import app
from flask import url_for, request, session, redirect

# Set Migration Directory for DB & DB info
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI ='mysql+gaerdbms:///type_db?instance=cloud-9209:type-instance',
    migration_directory = 'migrations'
))
app.config.from_envvar('TYPE_DESIGN_ALPHA', silent=True)