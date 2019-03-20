from bs4 import BeautifulSoup
import requests
import csv
import scrape
import re

URLS = []


i = 0
while i < 2:
    URLS = scrape.grab_urls('list.html', URLS)
    print(len(URLS))
    i += 1

# with open('list.html') as list_html:
#     soup = BeautifulSoup(list_html, 'lxml')


# with open('test3.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# DATA = scrape.scrape_report(soup)

# csv_file = open('mls_scrape.csv', 'a')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(scrape.ROWS)
# csv_writer.writerow(DATA)
# csv_file.close()