# # -*- coding: utf-8 -*-
# from application import db
# from schema import *
# import logging

# def init_proj_items () :
#     proj_items = [
#         { 'title' : u"반흘림 고딕", 
#             'author' : u"한세정",
#             'author_thumbnail' : 'res/images/test.jpg',
#             'thumbnail' : 'res/images/test.jpg',
#             'description' : u"어떤 폰트인지에 대한 설명을 여기에 작성하게 되는 것입니다"
#         },
#         { 'title' : u"바람체" ,
#             'author' : u"이용제",
#             'author_thumbnail' : 'res/images/lyj.jpg',
#             'thumbnail' : 'res/images/test1.jpg',
#             'description' : u"바람.체는 옛날 책에 쓰인 한글에서 영감을 받았습니다. 우리 옛 책을 보면 한글은 지금보다 크게 쓰였고, 그래서 글꼴의 개성이 잘 나타납니다."
#         },
#         { 'title' : u"직선 순명조", 
#             'author' : u"조윤준",
#             'author_thumbnail' : 'res/images/jyj.jpg',
#             'thumbnail' : 'res/images/test2.jpg',
#             'description' : u"this will help me decide on fonts when im doing a project with text, i never know what to do"
#         },
#         { 'title' : u"명주실" ,
#             'author' : u"엄후영",
#             'author_thumbnail' : 'res/images/uhy.jpg',
#             'thumbnail' : 'res/images/test3.jpg',
#             'description' : u"후영후영 엄후영"
#         }

#     ]
#     for item in proj_items :
#         author = Author(
#             email = item['author'] + "@gmail.com",
#             password = "passwd" + item['author'],
#             name = item['author'],
#             profile_image = item['author_thumbnail']
#         )
#         logging.info("author.id : " + str(author.id))

#         db.session.add(author)
#         db.session.commit()

#         author_id = Author.query.filter(Author.name == item['author']).first().id
#         logging.info("author.id : " + str(author.id))
#         logging.info("author_id : " + str(author_id))
#         db.session.add(TypeProject(
#             category = 'READING',
#             title = item['title'],
#             thumbnail = item['thumbnail'],
#             description = item['description'],
#             author_id = author_id
#         ))
#         db.session.commit()

# def get_proj_items (len_of_elements) :
#     projects = TypeProject.query.filter().limit(len_of_elements)
#     logging.info(projects)
#     logging.info(type(projects))
#     proj_list = []
#     for prj in projects :
#         author = Author.query.filter(Author.id == prj.author_id).one()
#         proj_list.append(dict (
#             title = prj.title,
#             author = author.name,
#             author_thumbnail = author.profile_image,
#             thumbnail = prj.thumbnail,
#             description = prj.description
#         ))
#     return proj_list


