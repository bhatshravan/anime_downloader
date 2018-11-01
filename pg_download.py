import requests
from bs4 import BeautifulSoup
import cfscrape

r = requests.get("http://kissanime.ru/Anime/Fairy-Tail-2014")
url="http://kissanime.ru/Anime/Fairy-Tail-2014"

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


	scraper = cfscrape.create_scraper()
	content1 = scraper.get(url).content
	content = (content1).decode("utf-8")
	
	soup = BeautifulSoup(content, 'html.parser')
	video_mir1 = soup.find_all('a')



	
	f = open("output.html","wb")
	f.write(content1)
	for data in video_mir1:
		print(data['href'])
		
		#print("<a href='",data['href'],"'>",data['title'],"</a>   ",data['title'])
		#f.write("<a href='",data['href'],"'>",data['title'],"</a>   ",data['title'],"\n")

	
	
	f.close()

if __name__ == '__main__':
	kiss()