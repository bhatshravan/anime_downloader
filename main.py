import requests
from bs4 import BeautifulSoup
import sys
import cfscrape
import requests
import json
from flask import Flask

urls = ["https://www.masterani.me/anime/watch/2514-boruto-naruto-next-generations/","https://www.masterani.me/anime/watch/2816-boku-no-hero-academia-3rd-season"]
names = ["0. Boruto", "1. My hero"]
app = Flask(__name__)

@app.route('/')
def hello():
	return("Hello world")

def prints():
	print("Our list contains:\n")
	for index,datas in enumerate(names):
		print(datas)
	print("\n")
	ll = int(input("Please enter number:"))
	ep = int(input("Please enter episode:"))
	url = str(urls[ll])+str(ep)

	print(url,"\nQuering results:\n")
	scraper = cfscrape.create_scraper()
	content1 = scraper.get(url).content
	content = (content1).decode("utf-8")


	soup = BeautifulSoup(content, 'html.parser')

	video_mir1 = soup.find_all('video-mirrors')
	print(video_mir1)

	video_mir2 = str(video_mir1[0])
	video_mir3 = video_mir2.replace("<video-mirrors :mirrors='","").replace("'></video-mirrors>","")

	data = json.loads(video_mir3)

	url=""

	for index,datas in enumerate(data):
		embed_id= datas["embed_id"]
		name = datas["host"]["name"]
		quality = datas["quality"]
		embed_prefix = str(datas["host"]["embed_prefix"])
		embed_suffix = str(datas["host"]["embed_suffix"])
		if embed_suffix=="None":
			embed_suffix=""

		url=embed_prefix+embed_id+embed_suffix
		print(url,index,name,quality,"\n")

if __name__ == '__main__':
	app.run()
	#prints()