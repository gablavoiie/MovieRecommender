import pandas as pd

df3 = pd.read_csv("movie_data.csv")

import requests
from bs4 import BeautifulSoup

def image_url(index):
    query = str(df3.iloc[index,2]) + ' poster'
    url = 'https://www.google.com/search?q=' + query + '&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    image = soup.find('img')
    return image.get('src')

print(image_url(0))