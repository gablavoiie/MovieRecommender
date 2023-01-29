import pandas as pd
import requests
from bs4 import BeautifulSoup

df3 = pd.read_csv("movie_data.csv")

# returns poster image url from movie index
def image_url(title):
    query = title + ' poster'
    url = 'https://www.google.com/search?q=' + query + '&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    images = soup.findAll('img')
    return images[1].get('src')