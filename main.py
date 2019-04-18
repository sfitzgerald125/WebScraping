from bs4 import BeautifulSoup
import requests
import csv
import classes
import re

# variables we will collect
ROWS = [
    'mls_num', 'num_pictures', 'list_price', 'price_perANDoriginal_list_price', 'status', 'cdom', 'list_date',
    'dom', 'address', 'area', 'city', 'county', 'restrictions', 'subdivision', 'taxes', 'zoning1', 'has_hoa',
    'hoa_transfer', 'hoa_amenities', 'pre_market', 'school_dist', 'elem', 'jr_high', 'sr_high', 'total_sqfoot.text',
    'total_bedrooms.text', 'total_bath_full.text', 'total_bath_three_fourth.text', 'total_bath_half.text', 'total_family.text',
    'total_den.text', 'total_formal_living_room.text','total_kitchen_k.text', 'total_kitchen_b.text', 'total_kitchen_f.text',
    'total_kitchen_s.text', 'total_laundry.text', 'total_fireplace.text', 'htype', 'style', 'year_built', 'const_status',
    'effect_yr_built', 'acres', 'deck_patio', 'frontage', 'garage', 'side', 'carport', 'back', 'prkg_sp', 'irregular',
    'fin_bsmt', 'roof', 'bsmt', 'heating', 'garage_park', 'air_cond', 'driveway', 'floor', 'water', 'window_cov', 'water_shares',
    'has_pool', 'has_spa', 'community_pool', 'pool_feat', 'master_level', 'possession', 'senior_comm', 'exterior', 'animals',
    'has_solar', 'landscape', 'lot_facts', 'inclusions', 'terms', 'storage', 'utilities', 'zoning2', 'remarks', 'exterior_feat',
    'interior_feat', 'amenities', 'access_feat', 'agt_remarks', 'show_inst', 'owner', 'owner_type', 'contact', 'contact_type', 'l_agent',
    'l_office', 'l_broker', 'bac', 'dual_var', 'list_type', 'comm_type', 'wthdrwn_dt', 'off_mkt_dt', 'exp_dt',
]

cookie = '' # insert your cookie
host = 'www.utahrealestate.com'
user_agent = '' # insert user-agent

myScraper = classes.scrappy(cookie,host,user_agent)

# collect all urls to be scraped
while myScraper.page <= 358:
    print("finished scraping urls from page: " + myScraper.page) # just see progress as we go through all 358 pages
    soup = myScraper.request_next_page()
    myScraper.append_urls(soup)

# Create a csv to store urls
csv_file = open('urls.csv', 'w')
csv_writer = csv.writer(csv_file)

# Save urls to csv
urls = myScraper.urls
for url in urls:
    csv_writer.writerow(url)
print(f'finished printing urls to CSV')

# Collect all urls that need to be scraped
urls = []
with open('urls.csv', newline='') as csvfile:
    urlreader = csv.reader(csvfile, delimiter=' ')
    for row in urlreader:
        urls.append(', '.join(row))

csv_file.close() # Close urls.csv

# Create a new csv file to store data reports
csv_file = open('mls_scrape.csv', 'w')
csv_writer = csv_writer(csv_file)

# print csv header to mls_scrape.csv
csv_writer.writerow(ROWS)

# Print reports to mls_scrape.csv
i = 0
for url in urls:
    data = myScraper.scrape_report(url) # Scrape each page
    csv_writer.writerow(data)
    if i%10 == 0:
        print(i) # print what number we're on every 10 times to keep track
    i += 1

csv_file.close()