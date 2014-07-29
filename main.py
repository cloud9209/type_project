from flask import Flask, render_template, request
from urllib import urlopen
from bs4 import BeautifulSoup
import tweepy, json

app = Flask(__name__)
app.config['DEBUG'] = True
consumer_key = 'vDmORdLd8GK8FiPZ6QmqQmIUh'
consumer_secret = 'vTh3RFJGF1zDHofXrzqbyRqfAfIyHFFFMYeBkXPjtz8cB6Szz4'
access_token = '2543773620-5cofJGbEZ923jIxT2Ots7miLul7bANGqlgHO8u0'
access_token_secret = 'Tfy4QtDTFYq9qdWJA2oABfBLLRB60RLelgqhwmrYfeqnP'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

# -*- coding: utf-8 -*-

@app.route('/tweepy')
def tweepy():
	
	return render_template('tweepy.html')

@app.route('/tweepy_query', methods= ['POST', 'GET'])
def tweepy_query():
	
	if request.method == 'POST':
		query = request.form['query']
		results = api.search(q=query, count=10)

		tweet_content_list = []
		
		for result in results:
			tweet_content = {
			"user_name" : "",
			"text" : "",
			}
			tweet_content['user_name'] = result.user.screen_name
			tweet_content['text'] = result.text
			tweet_content_list.append(tweet_content)

		datas = json.dumps(tweet_content_list)
	
	return datas

@app.route('/webtoon')
def webtoon():
	data = urlopen('http://comics.nate.com/webtoon/detail.php?btno=64923&bsno=369672&category=1').read()
	soup = BeautifulSoup(data)
	img_src = []

	for img in soup.select('div.toonView img'):
		img_src.append(img['src'])
	
	return render_template('webtoon.html', images = img_src)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


@app.route('/ideada')
def ideada():
    """Return a friendly HTTP greeting."""
    return render_template('idea-index.html')



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

