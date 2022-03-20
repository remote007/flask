from urllib import response
import requests
import json
from bs4 import BeautifulSoup

def create_api_data():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)
    return response.json()

def create_quotes_dict(api_data):
    quotes = {}
    for data in api_data:
        if data["author"]:
            if not data["author"] in quotes:
                quotes[data["author"]] = []
            quotes[data["author"]].append(data["text"])

    return quotes