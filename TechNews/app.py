from flask import flask,render_template
from bs4 import BeautifulSoup
import requests

url ="https://www.businesstoday.in/technology/news"
req = requests.get(url)
soup = BeautifulSoup(req.content)