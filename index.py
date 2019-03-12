import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com')
contents = page.content

soup = BeautifulSoup(contents, 'html.parser')

print(soup.find_all('a'))

