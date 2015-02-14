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

app.config[    'GOOGLE_CLIENT_ID'] = "895405110794-br07tvijkpkn3ranupra2nd6ej6bqm4m.apps.googleusercontent.com"
app.config['GOOGLE_CLIENT_SECRET'] = "BXZkSIkfspr1q9sTDhl-KnGM"
app.config[     'FACEBOOK_APP_ID'] = "1565583957033107"
app.config[ 'FACEBOOK_APP_SECRET'] = "52299bf7deb0667971e011a9d7a06963"