# from Flask import flask,render_template
from bs4 import BeautifulSoup
import requests

url ="https://www.businesstoday.in/technology/news"
req = requests.get(url)
# soup.a for anchor tag and soup.find_all('a') to give a list of all anchor tags
soup = BeautifulSoup(req.content,"html.parser")
outerdata = soup.find_all("div",class_="widget-listing",limit=6) #