from application import db
from schema import Author, TypeProject
from flask import session

def add(data) :
	db.session.add( TypeProject (
		category = data['category'],
		title = data['project_title'],
		description = data['description'],
		author_id = session['author-id'] # like user-id
	))
	db.session.commit()

def load(num_of_projects_to_load = 10) :
	return TypeProject.query.filter().limit(num_of_projects_to_load)

def get_proj_items (len_of_elements) :
    projects = TypeProject.query.filter().limit(len_of_elements)
    logging.info(projects)
    logging.info(type(projects))
    proj_list = []
    for prj in projects :
        proj_list.append(dict (
            proj_name = prj.name,
            artist_name = prj.author.name,
            artist_profile_image = prj.author.profile_image,
            proj_thumbnail = prj.thumbnail,
            proj_description = prj.description
        ))
    return proj_list


