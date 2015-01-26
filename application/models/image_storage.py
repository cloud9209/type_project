from application import db
from google.appengine.api import files, images
import author, project, work, logging

ROOT = '/gs/type-storage'

# return success flag
def store(category, id, raw_image) :
    ''' extension check '''
    ext = raw_image.filename.split('.')[-1].lower()
    if ext not in ['png', 'jpg', 'jpeg'] : return False

    # VALID EXTENSION BELOW
    image = raw_image.read()
    _target_ = eval("%s.get('id', %d, 1)" % (category, id))

    ''' image '''
    image_name = '%s/%s/%d.%s' % (category, 'image', id, ext)
    if _target_.image != image_name : files.delete('%s/%s' % (ROOT, _target_.image))
    path_writable = files.gs.create('%s/%s' % (ROOT, image_name), mime_type = raw_image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file_ :
        _file_.write(image)
    files.finalize(path_writable)
    _target_.image = image_name

    ''' thumbnail '''
    thumbnail = images.resize(image, 200, 200)
    thumbnail_name = '%s/%s/%d.%s' % (category, 'thumbnail', id, ext)
    if _target_.thumbnail != thumbnail_name : files.delete('%s/%s' % (ROOT, _target_.thumbnail))
    path_writable = files.gs.create('%s/%s' % (ROOT, thumbnail_name), mime_type = raw_image.content_type, acl='public-read')
    with files.open(path_writable, 'ab') as _file_ :
        _file_.write(thumbnail)
    files.finalize(path_writable)
    _target_.thumbnail = thumbnail_name

    ''' commit '''
    db.session.commit()
    return True

def load(filename) :
    path = '%s/%s' % (ROOT, filename)
    with files.open(path, 'r') as _file_ :
        data = _file_.read()
    return data