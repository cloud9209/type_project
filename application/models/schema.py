# -*- coding: utf-8 -*-
from application import db
class Author(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    email           = db.Column(db.String(60)) # -> to Unique
    password        = db.Column(db.String(100))
    name            = db.Column(db.String(45))
    image           = db.Column(db.String(100), default = "")
    thumbnail       = db.Column(db.String(100), default = "")
    projects        = db.relationship('TypeProject', backref='Author', lazy='dynamic', cascade='all, delete-orphan')

class TypeProject(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    category        = db.Column(db.Enum('READING', 'DISPLAYING', 'LETTERING'))
    title           = db.Column(db.String(40))
    description     = db.Column(db.Text())
    image           = db.Column(db.String(100), default = "")
    thumbnail       = db.Column(db.String(100), default = "")
    author_id       = db.Column(db.Integer, db.ForeignKey('author.id'))
    author          = db.relationship('Author', foreign_keys = [author_id])
    history         = db.relationship('TypeWork', backref='type_project', lazy='dynamic', cascade='all, delete-orphan')
    comments        = db.relationship('TypeProjectComment', backref='type_project', lazy='dynamic', cascade='all, delete-orphan')
    likes           = db.relationship('TypeProjectLike', backref='type_project', lazy='dynamic', cascade='all, delete-orphan')

class TypeProjectComment(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    body            = db.Column(db.Text())
    creation_time   = db.Column(db.DateTime, default=db.func.now())
    project_id      = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project         = db.relationship('TypeProject', foreign_keys = [project_id])
    writer_id       = db.Column(db.Integer, db.ForeignKey('author.id'))
    writer          = db.relationship('Author', foreign_keys = [writer_id])
    modified        = db.Column(db.Boolean, default = '0', onupdate = '1')
    modified_time   = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

class TypeProjectLike(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    project_id      = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project         = db.relationship('TypeProject', foreign_keys = [project_id])
    liker_id        = db.Column(db.Integer, db.ForeignKey('author.id'))
    liker           = db.relationship('Author', foreign_keys = [liker_id])

class TypeWork(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    image           = db.Column(db.String(100), default = "")
    thumbnail       = db.Column(db.String(100), default = "")
    description     = db.Column(db.Text())
    date            = db.Column(db.DateTime, default=db.func.now())
    author_id       = db.Column(db.Integer, db.ForeignKey('author.id'))
    author          = db.relationship('Author', foreign_keys = [author_id])
    project_id      = db.Column(db.Integer, db.ForeignKey('type_project.id'))
    project         = db.relationship('TypeProject', foreign_keys = [project_id])
    comments        = db.relationship('TypeWorkComment', backref='type_work', lazy='dynamic', cascade='all, delete-orphan')
    likes           = db.relationship('TypeWorkLike', backref='type_work', lazy='dynamic', cascade='all, delete-orphan')

class TypeWorkComment(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    body            = db.Column(db.Text())
    creation_time   = db.Column(db.DateTime, default = db.func.now())
    work_id         = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    work            = db.relationship('TypeWork', foreign_keys = [work_id])
    writer_id       = db.Column(db.Integer, db.ForeignKey('author.id'))
    writer          = db.relationship('Author', foreign_keys = [writer_id])
    modified        = db.Column(db.Boolean, default = '0', onupdate = '1')
    modified_time   = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

class TypeWorkLike(db.Model) :
    id              = db.Column(db.Integer, primary_key = True)
    work_id         = db.Column(db.Integer, db.ForeignKey('type_work.id'))
    work            = db.relationship('TypeWork', foreign_keys = [work_id])
    liker_id        = db.Column(db.Integer, db.ForeignKey('author.id'))
    liker           = db.relationship('Author', foreign_keys = [liker_id])
