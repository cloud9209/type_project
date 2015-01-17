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

def set_profile_image(author_id, new_path) :
    author = Author.query.get(Author.id == author_id)
    old_path = author.profile_image
    if new_path == old_path :
        # Does Nothing
        return
    elif new_path == "" :
        # New
        author.profile_image = new_path
    else :
        # Clean-up old profile data & set new
        
        # CODE : CLEANUP

        author.profile_image = new_path
    db.session.commit()

# MAKE IT USABLE AS DECORATOR
def is_valid_login(email, passwd) :
    return Author.query.filter(
        Author.email == email,
        Author.password = db.func.md5(passwd)
    ).count() != 0

def get_author_by_attr (attr, value) :
    return Author.query.filter(Author.__attr__(attr) == value).all()
