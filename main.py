import requests
from bs4 import BeautifulSoup
import cfscrape
import requests
import json
from flask import Flask, request, render_template

urls = ["https://www.masterani.me/anime/watch/2514-boruto-naruto-next-generations/","https://www.masterani.me/anime/watch/2816-boku-no-hero-academia-3rd-season/"]
names = ["0. Boruto", "1. My hero"]
app = Flask(__name__)


global already_parsed
already_parsed = []

global input_taken
input_taken = []

@app.route('/')
def hello():
	#return render_template('inp.html')
	return ''' 
	<!DOCTYPE html>
<html>
	<head>
		<title>Episode streamer</title>
	</head>
	<body>
	<center>
		0.Boruto<br/>
		1.My hero<br/>
		<br/>
		<form method="POST">
			<input name="ll"><br/>
			<input name="ep"><br/>
			<input type="submit">
		</form>
	</center></body>
</html>'''

@app.route('/', methods=['POST'])
def my_form_post():
	ll = request.form['ll']
	ep = request.form['ep']


   
	processed_text = prints(ll,ep)
	return processed_text



def prints(ll,ep):

	#for index,datas in enumerate(names):
	#	print(datas)
	global input_taken
	global already_parsed

	ll=int(ll)
	ep=int(ep)
	
	bobo=-1
	url = str(urls[ll])+str(ep)

	
	for inp in input_taken:
		bobo+=1
		print(inp)
		print(already_parsed[bobo])
		if str(url)==str(inp):
			return already_parsed[bobo]
			break
	bobo=-1

	input_taken.append(url)

	print(url,"\nQuering results:\n")
		

	url2=""
	stringy=""

	
	try:

		scraper = cfscrape.create_scraper()
		content1 = scraper.get(url).content
		content = (content1).decode("utf-8")

		soup = BeautifulSoup(content, 'html.parser')
		video_mir1 = soup.find_all('video-mirrors')
		
		video_mir2 = str(video_mir1[0])

		video_mir3 = video_mir2.replace("<video-mirrors :mirrors='","").replace("'></video-mirrors>","")

		data = json.loads(video_mir3)
		stringy+='''	<!DOCTYPE html>
<html>
	<head>
		<title>Episode streamer</title>
	</head>
	<body>
	<center>'''
		stringy+=url+"<br/><br/>"

		found_rapid=0

		for index,datas in enumerate(data):
			embed_id= datas["embed_id"]
			name = datas["host"]["name"]
			quality = datas["quality"]
			embed_prefix = str(datas["host"]["embed_prefix"])
			embed_suffix = str(datas["host"]["embed_suffix"])

			if(str(name)=="Rapidvideo"):
				found_rapid=str(url2)

			if embed_suffix=="None":
				embed_suffix=""

			url2=embed_prefix+embed_id+embed_suffix
			#print(url2)
		

			stringy+="<br/><a href='"+str(url2)+"'>"+str(url2)+"</a> "+str(index)+" "+str(name)+" "+str(quality)
			print(url2,index,name,quality,"\n")
	
		if found_rapid!=0:
			stringy+="<br/><br/>Rapid video source is:<br/>"
			r = requests.get("https://www.rapidvideo.com/e/FT5OBW9GFR&q=720o")

			soup = BeautifulSoup(r.content, 'html.parser')
			video_mir1 = soup.find_all('source')

			for data in video_mir1:
				print("<a href='",data['src'],"'>",data['src'],"</a>   ",data['title'])
				stringy+=("<a href='"+str(data['src'])+"'>"+str(data['src'])+"</a>   "+str(data['title'])+"<br/><br/>")


		stringy+='''	</center></body>
</html>'''
	except Exception as e:
		stringy="Exception"
		print(e)

	already_parsed.append(stringy)


	if stringy=="":
		stringy="No found"

	return stringy
	

if __name__ == '__main__':
	app.run()