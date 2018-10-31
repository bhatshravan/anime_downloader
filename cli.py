import requests
from bs4 import BeautifulSoup
import cfscrape
import requests
import json
from flask import Flask, request, render_template

import sys
import argparse

urls = ["https://www.masterani.me/anime/watch/2514-boruto-naruto-next-generations/","https://www.masterani.me/anime/watch/2816-boku-no-hero-academia-3rd-season/","https://www.masterani.me/anime/watch/27-fairy-tail-2014/"]
names = ["0. Boruto", "1. My hero","2. Fairy tail"]



global already_parsed
already_parsed = []

global input_taken
input_taken = []


def my_form_post():
	#parser = argparse.ArgumentParser(description="A program for downloading anime")
	#parser.add_argument('-h',help="Current node number", type=int)

	
	ll = sys.argv[1]
	ep = sys.argv[2]
   
	prints(ll,ep)



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
		if str(url)==str(inp):
			print("Already parsed")
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

		
		stringy+=url+"<br/><br/>"

		found_rapid=" "

		for index,datas in enumerate(data):
			embed_id= datas["embed_id"]
			name = datas["host"]["name"]
			quality = datas["quality"]
			embed_prefix = str(datas["host"]["embed_prefix"])
			embed_suffix = str(datas["host"]["embed_suffix"])

			
			if embed_suffix=="None":
				embed_suffix=""

			url2=embed_prefix+embed_id+embed_suffix
			#print(url2)
		

			stringy+="<br/><a href='"+str(url2)+"'>"+str(url2)+"</a> "+str(index)+" "+str(name)+" "+str(quality)
			print(url2," ",index," ",name," ",quality,"\n")

			if(str(name)=="Rapidvideo"):
				found_rapid=str(url2)

			print(found_rapid)


		if found_rapid!=" ":
			stringy+="<br/><br/>Rapid video source is:<br/>"
			found_rapid+="&q=720o"
			print("Rapid source = ",found_rapid)
			
			r = requests.get(found_rapid)

			soup = BeautifulSoup(r.content, 'html.parser')
			video_mir1 = soup.find_all('source')

			for data in video_mir1:
				print(data['src']," , ",data['title'])

				stringy+=("<a href='"+str(data['src'])+"'>"+str(data['src'])+"</a>   "+str(data['title'])+"<br/><br/>")

		else:
			print("no parid boyes")
		


		stringy+='''h'''
	except Exception as e:
		stringy="Exception"
		print(e)

	already_parsed.append(stringy)


	if stringy=="":
		stringy="No found"

	
	

if __name__ == '__main__':
	my_form_post()