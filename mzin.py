import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://survivor.fandom.com/wiki/Survivor:_China').text

soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())

