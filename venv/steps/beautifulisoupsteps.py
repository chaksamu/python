import requests
from bs4 import BeautifulSoup


url = str(input("Enter the URL"))

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
