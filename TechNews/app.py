from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__) 
@app.route("/",methods=["Get","POST"]) #@ means decorate , it is always above a function
def index() :

    url ="https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    # soup.a for anchor tag and soup.find_all('a') to give a list of all anchor tags
    soup = BeautifulSoup(req.content,"html.parser")
    outerdata = soup.find_all("div",class_="widget-listing",limit=6) 
    finalnews =""
    for news in outerdata:
        finalnews +="\u2022 "+news.div.div.a["title"]+"\n"
    print(finalnews)    

    return render_template("index.html",NEWS=finalnews)