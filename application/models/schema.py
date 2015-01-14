# -*- coding: utf-8 -*-
from application import db
class Author(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    email           = db.Column(db.String(60))
    password        = db.Column(db.String(100))
    
    name        = db.Column(db.String(45))
    profile_image   = db.Column(db.String(100))
    repositories    = db.relationship('TypeProject', backref='Author', lazy='dynamic')

class TypeProject(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    font_type       = db.Column(db.Enum('READING', 'DISPLAYING'))
    font_name       = db.String(db.String(40))
    font_title_image = db.String(db.String(100))
    font_title_description = db.Column(db.Text())

    font_author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    work_history   = db.relationship('FontWork', backref='TypeProject', lazy='dynamic')
    comments = db.relationship('CommentForRepository', backref='type_project', lazy='dynamic')

class CommentForRepository(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text())
    creation_time = db.Column(db.DateTime, default=db.func.now())
    repository_id = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('author.id'))

class FontWork(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    work_image = db.Column(db.String(100))
    work_description = db.Column(db.Text())
    cretion_time = db.Column(db.DateTime, default=db.func.now())
    comments = db.relationship('CommentForWork', backref='fontwork', lazy='dynamic')

class CommentForWork(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text())
    creation_time = db.Column(db.DateTime, default=db.func.now())
    Work_id = db.Column(db.Integer, db.ForeignKey('font_work.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('author.id'))