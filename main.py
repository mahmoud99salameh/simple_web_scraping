import requests
from bs4 import BeautifulSoup


def SimpleWebScraper(url):
    #sending request
    response=requests.get(url)
    #checking if its successfully connected
    if response.status_code==200:
        #parsing the html code 
        soup=BeautifulSoup(response.text,'html.parser')
        #extract the quotes 
        for i , quote in enumerate(quote,start=1):
            print(f"Quote {i} : {quote.text.strip()}")
    else:
        print("Error")
