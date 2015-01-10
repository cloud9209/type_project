# -*- coding: utf-8 -*-


proj_items = [
		{ 'proj_name' : '반흘림 고딕', 
			'artist_name' : '한세정',
			'artist_profile_image' : '',
			'proj_thumbnail' : '',
			'proj_description' : '어떤 폰트인지에 대한 설명을 여기에 작성하게 되는 것입니다'
		},
		{ 'proj_name' : '바람체' ,
			'artist_name' : '이용제',
			'artist_profile_image' : '',
			'proj_thumbnail' : '',
			'proj_description' : '바람.체는 옛날 책에 쓰인 한글에서 영감을 받았습니다. 우리 옛 책을 보면 한글은 지금보다 크게 쓰였고, 그래서 글꼴의 개성이 잘 나타납니다.'
		},
		{ 'proj_name' : '직선 순명조', 
			'artist_name' : '조윤준',
			'artist_profile_image' : '',
			'proj_thumbnail' : '',
			'proj_description' : 'this will help me decide on fonts when im doing a project with text, i never know what to do'
		},
		{ 'proj_name' : '명주실' ,
			'artist_name' : '엄후영',
			'artist_profile_image' : '',
			'proj_thumbnail' : '',
			'proj_description' : '후영후영 엄후영'
		}
	]
for proj_item in proj_items:
	print "프로젝트 이름 : ", proj_item['proj_name']
	print "아티스트 이름 : ", proj_item['artist_name']
	print "프로젝트 설명 : ", proj_item['proj_description']


