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

class _list(list) :
    def count(self) :
        return len(self)

@app.route('/')
def main() :
    projects = [
        dict(
            id = 1,
            category = 'READING',
            title = 'project-title',
            description = 'project-description',
            image = 'project-image',
            thumbnail = 'project-thumbnail',
            author_id = 1,
            author = dict (
                id = 1,
                name = 'name',
                thumbnail = 'thumbnail'
            ),
            history  = _list([ ]),
            comments = _list([ ]),
            likes    = _list([ ])
        )
    ]*10
    authors = []
    print projects
    print authors
    print render_template('main.html', projects = projects, authors = authors)
    return render_template('main.html', projects = projects, authors = authors)

@app.route('/sign_in', methods = ['GET', 'POST'])
def sign_in():
    print 'sign in'
    pass

@app.route('/project/<int:project_id>')
def type_project(project_id) :
    pass

@app.route('/image/<path:filename>')
def load_image(filename) :
    print filename
    return app.send_static_file('res/images/default_thumbnail.png')

@app.route('/project/<int:project_id>/like')
def like_project(project_id) :
    print project_id
    return 10

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

app.run(port = 8000)