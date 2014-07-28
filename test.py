from flask import Flask, render_template
from urllib import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://comics.nate.com/webtoon/detail.php?btno=64923&bsno=369672&category=1').read()
soup = BeautifulSoup(data)
img_src = []

for img in soup.select('div.toonView img'):
	img_src.append(img['src'])

return render_template('webtoon.html', images = img_src)
