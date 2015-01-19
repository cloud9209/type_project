from application import db
from schema import Author
import logging, auth

def add(data) :
    db.session.add( Author (
        email = data['email'],
        password = db.func.md5(data['password']),
        name = data['name']
    ))
    db.session.commit()

def add_exclusive(data) :
    _author = get('email', data['email'])
    logging.info("_author length : " + str(len(_author)))
    if len(_author) :
        return False
    else :
        add(data)
        return True

def get (attr, value, limit = -1) :
    author_filtered = Author.query.filter(getattr(Author, attr) == value)
    if   limit == 1 : return author_filtered.one()
    elif limit >  1 : return author_filtered.limit(limit)
    else            : return author_filtered.all()

""" TODO : Solve Circular import """
def get_secure (attr, value, limit = -1) :
    if not auth.secure() : return None
    author_filtered = Author.query.filter(getattr(Author, attr) == value)
    if   limit == 1 : return author_filtered.one()
    elif limit >  1 : return author_filtered.limit(limit)
    else            : return author_filtered.all()

# form has 'email' & 'password' attribute
def verified(form) : 
    return Author.query.filter(
        Author.email == form['email'],
        Author.password == db.func.md5(form['password'])
    ).count() != 0

# def set_profile_image(author_id, new_path) :
#     author = Author.query.get(Author.id == author_id)
#     old_path = author.profile_image
#     if new_path == old_path :
#         # Does Nothing
#         return
#     elif new_path == "" :
#         # New
#         author.profile_image = new_path
#     else :
#         # Clean-up old profile data & set new
        
#         # CODE : CLEANUP

#         author.profile_image = new_path
#     db.session.commit()



