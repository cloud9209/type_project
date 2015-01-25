from application import db
from google.appengine.api import files
import author, project, work, logging

def store_author_image(author_id, image) : # ( int, image ) -> |
    image_data = image.read()
    _author = author.get('id', author_id, 1)
    ''' original image '''
    filename = '%s/%d.%s' % ('image', author_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/author', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(image_data)
    files.finalize(path_writable)
    _author.image = filename
    
    '''resized image'''
    # resize & save as thumbnail
    thumbnail_data = image_data
    filename = '%s/%d.%s' % ('thumbnail', author_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/author', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(thumbnail_data)
    files.finalize(path_writable)
    _author.thumbnail = filename

    '''commit change'''
    db.session.commit()

def load_author_image(filename) : # ( str ) -> image
    path = '%s/%s' % ('/gs/type-storage/author', filename)
    with files.open(path, 'r') as _file :
        data = _file.read()
    return data

def store_project_image(project_id, image) : # ( int, image ) -> |
    image_data = image.read()
    _project = project.get('id', project_id, 1)
    ''' original image '''
    filename = '%s/%d.%s' % ('image', project_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/project', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(image_data)
    files.finalize(path_writable)
    _project.image = filename
    
    '''resized image'''
    # resize & save as thumbnail
    thumbnail_data = image_data
    filename = '%s/%d.%s' % ('thumbnail', project_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/project', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(thumbnail_data)
    files.finalize(path_writable)
    _project.thumbnail = filename

    '''commit change'''
    db.session.commit()

def load_project_image(filename) : # ( str ) -> image
    path = '%s/%s' % ('/gs/type-storage/project', filename)
    logging.debug(filename)
    logging.debug(path)
    with files.open(path, 'r') as _file :
        data = _file.read()
    return data

def store_work_image(work_id, image) : # ( int, image ) -> |
    image_data = image.read()
    _work = work.get('id', work_id, 1)
    ''' original image '''
    filename = '%s/%d.%s' % ('image', work_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/work', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(image_data)
    files.finalize(path_writable)
    _work.image = filename
    
    '''resized image'''
    # resize & save as thumbnail
    thumbnail_data = image_data
    filename = '%s/%d.%s' % ('thumbnail', work_id, image.filename.split('.')[-1])
    path = '%s/%s' % ('/gs/type-storage/work', filename)
    path_writable = files.gs.create(path, mime_type = image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file :
        _file.write(thumbnail_data)
    files.finalize(path_writable)
    _work.thumbnail = filename

    '''commit change'''
    db.session.commit()

def load_work_image(filename) : # ( str ) -> image
    path = '%s/%s' % ('/gs/type-storage/work', filename)
    with files.open(path, 'r') as _file :
        data = _file.read()
    return data