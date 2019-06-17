import requests
import urllib.request
import time
import csv

from bs4 import BeautifulSoup
from prettytable import PrettyTable

start = time.time()


def get_product_info(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    product_title = soup.find("h1", {"class": "products_info_name"})

    title = product_title.select('span')[0]

    print(title.text)

    product_image = soup.find("div", {"class": "product-info-bild"})

    image = product_image.select('a[href]')[0].get('href')

    image = "https://www.tintenalarm.de/" + image

    print(image)

    manufacturer_div = soup.find('div', {'itemprop': 'manufacturer'})

    manufacturer = manufacturer_div.text.strip()

    print(manufacturer)

    product_price = soup.find('div', {'class': 'product-info-preis'})

    price = product_price.text.strip()

    price = price.split(" ")[0]

    print(price)

    product_feature = soup.findAll('div', {'class': 'products_features_list'})[1]

    product_type = product_feature.select('span')[0].text.strip()

    print(product_type)

    product_feature = soup.findAll('div', {'class': 'products_features_list'})[4]

    # oem = product_feature.select('div')[0].text.split("-")[1]

    oem = product_feature.select('div')[0].text

    print(oem)

    data = str(oem) + "~" + str(manufacturer) + "~" + str(title.text) + "~" + str(product_type) + "~" + str(
        price) + "~" + str(image)

    return data
