from bs4 import BeautifulSoup
import requests
import csv
import classes
import re

myScraper = classes.scrappy()

while myScraper.next_page < 2:
    soup = myScraper.request_next_page(myScraper.next_page)
    myScraper.grab_urls(soup)


# DATA = myScraper.scrape_report(soup)

# csv_file = open('mls_scrape.csv', 'a')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(scrape.ROWS)
# csv_writer.writerow(DATA)
# csv_file.close()