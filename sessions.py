import requests
from bs4 import BeautifulSoup



with requests.Session() as s:
    r = s.get('https://www.utahrealestate.com/search/perform/md/undefined/recent/1', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    print(soup.prettify())