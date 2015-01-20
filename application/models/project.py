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

def get(attr = None, value = None, limit = -1) :
    projects = None
    if (attr, value) == (None, None) : projects = TypeProject.query.filter()
    else                             : projects = TypeProject.query.filter(getattr(TypeProject, attr) == value)

    if  limit == 1 : projects = [projects.one()] # ONE? FIRST?
    if  limit >  1 : projects = projects.limit(limit)
    else           : projects = projects.all()

    ret_projects = []
    for project in projects :
        ret_projects.append(dict  (
            title            = project.title,
            author           = project.author.name,
            author_thumbnail = project.author.profile_image,
            thumbnail        = project.thumbnail,
            description      = project.description,
            category         = project.category
        ))
    return ret_projects