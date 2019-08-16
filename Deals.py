from bs4 import BeautifulSoup 
from csv import writer
import requests 

response = requests.get('https://www.ebay.co.uk/deals')

soup = BeautifulSoup(response.text,'html.parser')

#It collects all the tag classes that have the following name
deals = soup.find_all(class_="ebayui-dne-item-featured-card")

#print(deals)
items_names = []

for deal in deals:
    sections = deal.find_all(class_="col")
    for section in sections:
        blocks = section.find_all(class_="dne-itemtile-detail")
        for block in blocks:
            title = block.findAll(class_="dne-itemtile-title")
            print(title[0]["title"])
            # used to add the items in to a list
            # items.append(title)

#print(items[0]["title"])
