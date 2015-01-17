from application import db
from schema import Author, TypeProject
from flask import session

def add(data) :
	db.session.add( TypeProject (
		category = data['category'],
		title = data['project_title'],
		description = data['description'],
		author_id = session['author-id']
	))
	db.session.commit()

def load(num_of_projects_to_load = 10) :
	return TypeProject.query.filter().limit(num_of_projects_to_load)

def get_proj_items (len_of_elements) :
    projects = load(len_of_elements)
    proj_list = []
    for prj in projects :
        proj_list.append(dict (
            title = prj.title,
            author = prj.author.name,
            author_thumbnail = prj.author.profile_image,
            thumbnail = prj.thumbnail,
            description = prj.description,
            category = prj.category
        ))
    return proj_list


