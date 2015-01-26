from application import db
from google.appengine.api import files, images
import author, project, work, logging

BUCKET_NAME = 'type-storage'

def store(category, id, raw_image) :
    image = raw_image.read()
    _target_ = eval("%s.get('id', %d, 1)" % (category, id))
    '''original image'''
    filename = '%s/%d.%s' % ('image', id, raw_image.filename.split('.')[-1])
    path = '/gs/%s/%s/%s' % (BUCKET_NAME, category, filename)
    path_writable = files.gs.create(path, mime_type = raw_image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file_ :
        _file_.write(image)
    files.finalize(path_writable)
    _target_.image = filename

    '''resized image'''
    thumbnail = images.resize(image, 200, 200)
    filename = '%s/%d.%s' % ('thumbnail', id, raw_image.filename.split('.')[-1])
    path = '/gs/%s/%s/%s' % (BUCKET_NAME, category, filename)
    path_writable = files.gs.create(path, mime_type = raw_image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file_ :
        _file_.write(thumbnail)
    files.finalize(path_writable)
    _target_.thumbnail = filename

    '''commit'''
    db.session.commit()

def load(category, filename) :
    path = '/gs/%s/%s/%s' % (BUCKET_NAME, category, filename)
    with files.open(path, 'r') as _file_ :
        data = _file_.read()
    return data