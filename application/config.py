from application import app
from flask import url_for, request, session, redirect

# Set Migration Directory for DB & DB info
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI ='mysql+gaerdbms:///scrap_scrap?instance=id-scrap-scrap:scrap-scrap',
    migration_directory = 'migrations'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)