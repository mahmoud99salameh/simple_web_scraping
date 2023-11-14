import requests
from bs4 import BeautifulSoup


def SimpleWebScraper(url):
    #sending request
    response=requests.get(url)
    #checking if its successfully connected
    if response.status_code==200:
        