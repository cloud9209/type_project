from application import db
from schema import author

class AuthorManager(object) :
	

def add_author(data) :
	author = Author(
		email = data['email'],
		password = db.func.md5(data['password']),
		name = data['name']
	)
	db.session.add(author)
	db.session.commit()

def add_profile_image(author_id, filename):
	author = get_author_by_id(author_id)
	author.profile_image = filename
	db.session.commit()

def change_profile(author_id, new_data):
	data = get_author_by_id(author_id)
	data.name = new_data['name']
	data.school = new_data['school']
	db.session.commit()

def change_password(author_id, new_data):
	data = get_author_by_id(author_id)
	data.password = db.func.md5(new_data['new_password'])
	db.session.commit()

def change_password2(author_id, new_pw):
	data = get_author_by_id(author_id)
	data.password = db.func.md5(new_pw)
	db.session.commit()

def login_check(email, password):
	return Author.query.filter(Author.email == email, Author.password == db.func.md5(password)).count() != 0

def password_check(author_id, password):
	return Author.query.filter(Author.id == author_id, Author.password == db.func.md5(password)).count() != 0

def get_author_by_id(author_id):
	return Author.query.get(author_id)

def get_author_by_id_lst(id_lst):
	authors = Author.query.filter(Author.id.in_(id_lst)).all()
	return authors

def get_author_by_email(email):
	return Author.query.filter(Author.email == email).all()

def get_author_by_name(string):
	return Author.query.filter(Author.name.like("%"+string+"%")).all()

def get_names_by_id_lst(id_lst):
	lst = []
	authors = Author.query.filter(Author.id.in_(id_lst)).all()
	for author in authors:
		lst.append(author.name)
	return lst