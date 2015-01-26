from flask import Flask

app = Flask('application')
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI ='mysql+gaerdbms:///type_db?instance=cloud-9209:typedesign-instance',
    migration_directory = 'migrations'
))
app.config.from_envvar('TYPE_DESIGN_ALPHA', silent=True)

from flask import render_template, session, url_for, request, redirect, abort
import logging

@app.route('/')
def main() :
    projects, authors = [
        dict(
            author = dict(
                name = 'hi'
            ),
            thumbnail = 'agaewgaewgew'
        )
    ], []
    return render_template('main.html', projects = projects, authors = authors)
@app.route('/agewga')
def sign_in():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

app.run()