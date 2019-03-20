import requests
from bs4 import BeautifulSoup


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__utmc=41202813; __utmz=41202813.1553106212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ureBrowserSession=1553123150368895489500; _gcl_au=1.1.1217016442.1553123151; __utma=41202813.623660756.1553106212.1553116294.1553123151.3; __gads=ID=2c13cb39f6d4b3b5:T=1553123150:S=ALNI_MY5y4hpO7v9WKtYXQaelQ9cTbj0pA; _ga=GA1.2.623660756.1553106212; _gid=GA1.2.2135618890.1553123153; __qca=P0-1804500325-1553123154710; OX_plg=pm; ureServerSession=1553123150368895489500; PHPSESSID=j93697h1k28f4l1c9b2oj5gai2; btpdb.6EeDEhH.dGZjLjQ4NTE4NA=UkVRVUVTVFMuMTI; HELP_RIGHTS=1; __utmv=41202813.Member; __utmt=1; __utmb=41202813.24.10.1553123151',
    'Host': 'www.utahrealestate.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

with requests.Session() as s:
    url = 'https://www.utahrealestate.com/'
    r = s.get(url, headers=headers)
    r = s.get('https://www.utahrealestate.com/report/display/report/full/type/1/in_pop/1/listno/1505790/force//actor/', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    print(soup.prettify())
    
    
