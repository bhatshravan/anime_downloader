import requests
from bs4 import BeautifulSoup
import cfscrape

r = requests.get("http://kissanime.ru/Anime/Fairy-Tail-2014")
url="http://192.168.1.2:8080/output.html"

#print(r.content)

def mira():

	soup = BeautifulSoup(r.content, 'html.parser')
	video_mir1 = soup.find_all('source')

	for data in video_mir1:
		print("<a href='",data['src'],"'>",data['src'],"</a>   ",data['title'])

	f = open("output.html","wb")
	f.write(r.content)
	f.close()

def kiss():
	
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
	print(str(s3))
	
	
	
	#f = open("output.html","wb")
	#f.write(content1)
	#for data in video_mir1:
	#print(data['href'])
	
	#print("<a href='",data['href'],"'>",data['title'],"</a>   ",data['title'])
	#f.write("<a href='",data['href'],"'>",data['title'],"</a>   ",data['title'],"\n")

	
	
	#f.close()

if __name__ == '__main__':
	kiss()