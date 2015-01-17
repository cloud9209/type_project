# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from application import app

@app.route('/')
def main():
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
		},
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
		},
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
		},
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
		}

	]

	return render_template("main.html", proj_items = proj_items)

@app.route('/inside_proj', methods=['POST'])
def inside_proj():
	if request.method == 'POST':
		paper_items = [
			{ 'date' : u"2014년 6월 7일 14시 20분", 
				'thumbnail' : 'res/images/process_test_6.jpg',
				'description' : u"어려웧ㅎㅎ"
			},
			{ 'date' : u"2014년 6월 7일 14시 20분", 
				'thumbnail' : 'res/images/process_test_6.jpg',
				'description' : u"어려웧ㅎㅎ"
			},
			{ 'date' : u"2014년 6월 7일 14시 20분", 
				'thumbnail' : 'res/images/process_test_6.jpg',
				'description' : u"어려웧ㅎㅎ"
			},
			{ 'date' : u"2014년 6월 7일 14시 20분", 
				'thumbnail' : 'res/images/process_test_6.jpg',
				'description' : u"어려웧ㅎㅎ"
			},
			{ 'date' : u"2014년 6월 7일 14시 20분", 
				'thumbnail' : 'res/images/process_test_6.jpg',
				'description' : u"어려웧ㅎㅎ"
			}		
		]

	return render_template('paper_items.html', paper_items = paper_items)
