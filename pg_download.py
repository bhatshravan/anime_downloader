import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.rapidvideo.com/e/FT5OBW9GFR&q=720o")

#print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
video_mir1 = soup.find_all('source')

for data in video_mir1:
	print("<a href='",data['src'],"'>",data['src'],"</a>   ",data['title'])

f = open("output.html","wb")
f.write(r.content)
f.close()