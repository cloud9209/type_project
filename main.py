from flask import Flask, render_template
from urllib import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
# -*- coding: utf-8 -*-
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

