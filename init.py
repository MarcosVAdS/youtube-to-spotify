from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

driver = webdriver.Chrome("C:/Users/suporte/Downloads/chromedriver_win32/chromedriver.exe")

musicArtist = []
musicName = []
musicLink = []
driver.get("https://www.youtube.com/playlist?list=PL0ao6cotJFFUgKFlnkidAO7S5pWXQtiLB")

pageContent = driver.page_source
soup = BeautifulSoup(pageContent, features='html.parser')

for a in soup.findAll('div', attrs={'class': 'style-scope ytd-playlist-video-renderer'}):
    if (a.find('span', attrs={'class': 'style-scope ytd-playlist-video-renderer'}) == None):
        pass
    else:
        title = a.find('span', attrs={'class': 'style-scope ytd-playlist-video-renderer'}).text
    musicName.append(title)

musics = []
for element in musicName:
    musics.append(element.strip())

musicsFormated = list(dict.fromkeys(musics))


df = pd.DataFrame({'musicas ': musicsFormated})
df.to_json('musicsSertanejo.json', index=False, orient="split")
df.to_csv('musicsSertanejo.csv', index=False, encoding="utf8")
