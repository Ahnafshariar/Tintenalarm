import requests
import urllib.request
import time
import csv

from bs4 import BeautifulSoup
from prettytable import PrettyTable

start = time.time()

with open("tintealarm_product_url.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        print(lines[8])
