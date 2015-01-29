from application import app
from flask import render_template, url_for, request, redirect, jsonify, send_file
from application.models import auth, image_storage
import logging

''' Download'''
@app.route('/image/')
@auth.requires(auth.type.author)
def load_default_image() :
    return app.send_static_file('res/images/default_thumbnail.png')

@app.route('/image/<path:filename>')
@auth.requires(auth.type.author)
def load_image(filename) : 
    if filename.split('/')[0] not in ['author', 'project', 'work'] :
        logging.error('Inavalid image path : ' + filename)
        raise
    try :
        return image_storage.load(filename)
    except :
        return app.send_static_file('res/images/default_%s.png' % filename.split('/')[1])

''' Upload '''
@app.route('/author/<int:author_id>/upload', methods = ['POST'])
@auth.requires(auth.type.author)
def upload_author_image(author_id) :
    success = image_storage.store('author', author_id, request.files['author-image'])
    if success : return jsonify( success = True , action = 'redirect', body = url_for('type_author', author_id = author_id))
    else       : return jsonify( success = False, action = 'alert', body = 'Failed to upload author profile-image' )

@app.route('/project/<int:project_id>/upload', methods = ['POST'])
#@auth.requires(auth.type.project)
def upload_project_image(project_id) :
    success = image_storage.store('project', project_id, request.files['project-image'])
    if success : return jsonify( success = True , action = 'redirect', body = url_for('type_project', project_id = project_id))
    else       : return jsonify( success = False, action = 'alert', body = 'Failed to upload project image' )

@app.route('/work/<int:work_id>/upload', methods = ['POST'])
@auth.requires(auth.type.work)
def upload_work_image(work_id) :
    success = image_storage.store('work', work_id, request.files['work-image'])
    if success : return jsonify( success = True , action = 'redirect', body = url_for('type_work', work_id = work_id))
    else       : return jsonify( success = False, action = 'alert', body = 'Failed to upload work image' )