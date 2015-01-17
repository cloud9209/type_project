# -*- coding: utf-8 -*-
from application import db
from schema import *
import logging

def init_proj_items () :
    proj_items = [
        { 'proj_name' : u"반흘림 고딕", 
            'artist_name' : u"한세정",
            'artist_profile_image' : 'res/images/test.jpg',
            'proj_thumbnail' : 'res/images/test.jpg',
            'proj_description' : u"어떤 폰트인지에 대한 설명을 여기에 작성하게 되는 것입니다"
        },
        { 'proj_name' : u"바람체" ,
            'artist_name' : u"이용제",
            'artist_profile_image' : 'res/images/lyj.jpg',
            'proj_thumbnail' : 'res/images/test1.jpg',
            'proj_description' : u"바람.체는 옛날 책에 쓰인 한글에서 영감을 받았습니다. 우리 옛 책을 보면 한글은 지금보다 크게 쓰였고, 그래서 글꼴의 개성이 잘 나타납니다."
        },
        { 'proj_name' : u"직선 순명조", 
            'artist_name' : u"조윤준",
            'artist_profile_image' : 'res/images/jyj.jpg',
            'proj_thumbnail' : 'res/images/test2.jpg',
            'proj_description' : u"this will help me decide on fonts when im doing a project with text, i never know what to do"
        },
        { 'proj_name' : u"명주실" ,
            'artist_name' : u"엄후영",
            'artist_profile_image' : 'res/images/uhy.jpg',
            'proj_thumbnail' : 'res/images/test3.jpg',
            'proj_description' : u"후영후영 엄후영"
        }

    ]
    for item in proj_items :
        author = Author(
            email = item['artist_name'] + "@gmail.com",
            password = "passwd" + item['artist_name'],
            name = item['artist_name'],
            profile_image = item['artist_profile_image']
        )
        logging.info("author.id : " + str(author.id))

        db.session.add(author)
        db.session.commit()

        author_id = Author.query.filter(Author.name == item['artist_name']).first().id
        logging.info("author.id : " + str(author.id))
        logging.info("author_id : " + str(author_id))
        db.session.add(TypeProject(
            category = 'READING',
            name = item['proj_name'],
            thumbnail = item['proj_thumbnail'],
            description = item['proj_description'],
            author_id = author_id
        ))
        db.session.commit()

def get_proj_items (len_of_elements) :
    projects = TypeProject.query.filter().limit(len_of_elements)
    logging.info(projects)
    logging.info(type(projects))
    proj_list = []
    for prj in projects :
        author = Author.query.filter(Author.id == prj.author_id).one()
        proj_list.append(dict (
            proj_name = prj.name,
            artist_name = author.name,
            artist_profile_image = author.profile_image,
            proj_thumbnail = prj.thumbnail,
            proj_description = prj.description
        ))
    return proj_list


