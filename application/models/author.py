from application import db
from schema import Author
from flask import session, request
from attrdict import attrdict
import logging, image_storage

def add(data, auth_type) :
    if auth_type == 'GOOGLE' :
        db.session.add( Author (
            email = data['email'],
            name = data['name'],
            image = data['picture'],
            thumbnail = data['picture'],
            googleplus_id = data['id']
        ))
    elif auth_type == 'FACEBOOK' :
        logging.critical('models.author.add : Not Implemented for FACEBOOK OAuth')
        return #
        db.session.add( Author (
            email = data['email'],
            name = data['name'],
            image = "http://graph.facebook.com/%s/picture" % data['id'],
            thumbnail = "http://graph.facebook.com/%s/picture" % data['id'],
            facebook_id = data['id']
        ))
    elif auth_type is None :
        # TODO : Autho register thumbnail
        db.session.add( Author (
            email = data['email'],
            password = db.func.md5(data['password']),
            name = data['name']
        ))
    else :
        logging.critical('models.author.add : Unrechable branch')
    db.session.commit()

def add_exclusively(data, auth_type = None) :
    success = True
    account = get('email', data['email'], 1)
    if account is None : 
        add(data, auth_type)
        return success

    was_external_image_source = account.image.split('/')[0] not in ['author', 'project', 'work']
    if auth_type is 'GOOGLE' :
        if account.googleplus_id == '' or account.googleplus_id == data['id'] :
            if was_external_image_source :
                account.image     = data['picture']
                account.thumbnail = data['picture']
            account.googleplus_id = data['id']
            db.session.commit()
        else :
            success = False # Other id binded to the email
    elif auth_type is 'FACEBOOK' :
        if account.facebook_id == '' or account.facebook_id == data['id'] :
            if was_external_image_source :
                account.image     = "http://graph.facebook.com/%s/picture" % data['id']
                account.thumbnail = "http://graph.facebook.com/%s/picture" % data['id']
            account.facebook_id   = data['id']
            db.session.commit()
        else :
            success = False # Other id binded to the email
    elif account.password == '' :
        account.password = db.func.md5(data['password'])
        db.session.commit()
    else :
        success = False
    return success

def get (attr = None, value = None, limit = -1) :
    authors = None
    if (attr, value) == (None, None) : authors = Author.query.filter()
    else                             : authors = Author.query.filter(getattr(Author, attr) == value)

    if limit == 1 :
        try    : return authors.one()
        except : return None        
    elif limit >  1 : return authors.limit(limit)
    else            : return authors.all()

def secure() :
    safe, action, body = None, ['alert', 'abort'][request.method=='GET'], None
    if 'author_id' not in session :
        safe = False
        body = 'Not Authorized : Invalid Access Sequence'
    else :
        if session['author_id'] == session['user_id'] :
            safe = True
        else :
            safe = False
            body = 'Not Authorized'
    return attrdict( safe = safe, action = action, body = body )
