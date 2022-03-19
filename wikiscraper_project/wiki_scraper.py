import requests
import json
from bs4 import BeautifulSoup

def create_api_data():
    url = "https://type.fit/api/quotes"
    