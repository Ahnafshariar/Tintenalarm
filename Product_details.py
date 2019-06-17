import requests
import urllib.request
import time
import csv

from bs4 import BeautifulSoup
from prettytable import PrettyTable

start = time.time()

url = 'https://www.tintenalarm.de/10-farbbaender-von-tintenalarm.de-ersetzt-canon-ep-102-4202a002-schwarz-rot-p-28970.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

product_title = soup.find('span', attrs={'itemprop': 'name'})

title = product_title.text

print(title)


img_link = soup.a.img['src']

print(img_link)
