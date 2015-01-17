from application import db
from schema import Author

def add(data) :
    db.session.add( Author (
        email = data['email'],
        password = db.func.md5(data['password']),
        name = data['name']
    ))
    db.session.commit()
    # TODO : db.session.add(obj).commit() availiable ?

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

# form has 'email' & 'password' attribute
def verify(form) : 
    return Author.query.filter(
        Author.email == form['email'],
        Author.password == db.func.md5(form['password'])
    ).count() != 0

def get (attr, value) :
    return Author.query.filter(getattr(Author, attr) == value).all()