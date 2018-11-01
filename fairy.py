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
fairy=["http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-102?id=124131&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-101?id=123909&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-100?id=123694&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-099?id=123443&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-098?id=123132&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-097?id=122798&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-096?id=122582&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-095?id=122457&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-094?id=122311&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-093?id=122163&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-092?id=121931&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-091?id=121759&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-090?id=121399&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-089?id=121131&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-088?id=120807&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-087?id=120489&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-086?id=120193&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-085?id=119900&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-084?id=119581&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-083?id=119170&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-082?id=118902&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-081?id=118635&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-080?id=118289&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-079?id=117957&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-078?id=117564&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-077?id=117157&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-076?id=116913&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-075?id=116735&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-074?id=116483&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-073?id=115727&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-072?id=115231&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-071?id=114350&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-070?id=113710&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-069?id=113125&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-068?id=112722&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-067?id=112466&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-066?id=112092&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-065?id=111836&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-064?id=111582&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-063?id=111109&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-062?id=110662&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-061?id=110284&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-060?id=109881&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-059?id=109403&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-058?id=108595&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-057?id=108070&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-056?id=106601&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-055?id=105420&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-054?id=103310&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-053?id=102209&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-052?id=100692&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-051?id=98493&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-050?id=98492&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-049?id=98491&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-048?id=98490&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-047?id=98489&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-046?id=98488&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-045?id=98487&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-044?id=98486&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-043?id=98485&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-042?id=98484&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-041?id=98483&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-040?id=98482&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-039?id=98481&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-038?id=98480&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-037?id=98479&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-036?id=98478&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-035?id=98477&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-034?id=98476&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-033?id=98475&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-032?id=98474&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-031?id=98473&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-030?id=98472&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-029?id=98471&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-028?id=98470&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-027?id=98469&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-026?id=98468&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-025?id=98467&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-024?id=98466&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-023?id=98465&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-022?id=98464&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-021?id=98463&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-020?id=98462&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-019?id=98461&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-018?id=98460&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-017?id=98459&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-016?id=98458&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-015?id=98457&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-014?id=98456&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-013?id=98455&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-012?id=98454&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-011?id=98453&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-010?id=98452&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-009?id=98451&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-008?id=98450&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-007?id=98449&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-006?id=98448&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-005?id=98447&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-004?id=98446&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-003?id=98445&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-002?id=98444&s=rapidvideo", "http://kissanime.ru/Anime/Fairy-Tail-2014/Episode-001?id=98443&s=rapidvideo"]


global already_parsed
already_parsed = []

global input_taken
input_taken = []


def my_form_post():

	
	ep = sys.argv[1]
   
	prints(ep)



def prints(ep):

	global input_taken
	global already_parsed

	ep=int(ep)
	
	bobo=-1
	url = str(fairy[len(fairy)-ep])
	
	
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
		found_rapid = kiss(url)

		stringy+="<br/><br/>Rapid video source is:<br/>"
		print(found_rapid)
		found_rapid+="&q=720o"
		print(found_rapid)
		r = requests.get(found_rapid)

		soup = BeautifulSoup(r.content, 'html.parser')
		video_mir1 = soup.find_all('source')

		for data in video_mir1:
			print(data['src'],"-> ",data['title'])
			stringy+=(data['src']+"-> "+data['title'])

		already_parsed.append(stringy)

	except Exception as e:
		stringy="Exception"
		print(e)


	if stringy=="":
		stringy="No found"

		

		
def kiss(url):
	
	print("Started query")

	scraper = cfscrape.create_scraper()
	content1 = scraper.get(url).content
	content = (content1).decode("utf-8")
	
	#print(content1)
	
	soup = BeautifulSoup(content, 'html.parser')
	#video_mir1 =soup.find("iframe", {"id": "my_video_1"})


	#print(video_mir1)
	
	s1 = content1.split(("; border: 0px;\" src=\"").encode())
	s2 = s1[1].split(("\" allowfullscreen=\"true").encode())
	
	s3 = s2[0].decode("utf-8")
	return (str(s3))

if __name__ == '__main__':
	my_form_post()