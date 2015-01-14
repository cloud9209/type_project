# -*- coding: utf-8 -*-
from application import db
class Author(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    email               = db.Column(db.String(60))
    password            = db.Column(db.String(100))
    name                = db.Column(db.String(45))
    profile_image       = db.Column(db.String(100))
    projects            = db.relationship('TypeProject', backref='Author', lazy='dynamic')

class TypeProject(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    category            = db.Column(db.Enum('READING', 'DISPLAYING'))
    name                = db.String(db.String(40))
    description         = db.Column(db.Text())
    thumbnail         = db.String(db.String(100))
   
    author_id           = db.Column(db.Integer, db.ForeignKey('author.id'))
    history             = db.relationship('TypeWork', backref='type_project', lazy='dynamic')
    comments            = db.relationship('TypeProjectComment', backref='type_project', lazy='dynamic')

class TypeProjectComment(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    body                = db.Column(db.Text())
    creation_time       = db.Column(db.DateTime, default=db.func.now())
    project_id          = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    writer_id           = db.Column(db.Integer, db.ForeignKey('author.id'))

class TypeWork(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    image               = db.Column(db.String(100))
    description         = db.Column(db.Text())
    cretion_time        = db.Column(db.DateTime, default=db.func.now())
    project_id          = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    comments            = db.relationship('TypeWorkComment', backref='type_work', lazy='dynamic')

class TypeWorkComment(db.Model) :
    id                  = db.Column(db.Integer, primary_key = True)
    body                = db.Column(db.Text())
    creation_time       = db.Column(db.DateTime, default = db.func.now())
    work_id             = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    writer_id           = db.Column(db.Integer, db.ForeignKey('author.id'))