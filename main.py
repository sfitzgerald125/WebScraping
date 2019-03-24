from bs4 import BeautifulSoup
import requests
import csv
import classes
import re

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

cookie = '__utmz=41202813.1553106212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gcl_au=1.1.1217016442.1553123151; __gads=ID=2c13cb39f6d4b3b5:T=1553123150:S=ALNI_MY5y4hpO7v9WKtYXQaelQ9cTbj0pA; _ga=GA1.2.623660756.1553106212; _gid=GA1.2.2135618890.1553123153; __qca=P0-1804500325-1553123154710; PHPSESSID=hri7k7u7e79isjsr759vhm1h24; __utmc=41202813; OX_plg=pm; ureBrowserSession=1553179469556924025500; __utma=41202813.623660756.1553106212.1553176955.1553179470.7; __utmt=1; ureServerSession=1553179469556924025500; btpdb.6EeDEhH.dGZjLjQ4NTE4NA=UkVRVUVTVFMuMTY; HELP_RIGHTS=1; __utmv=41202813.Member; __utmb=41202813.6.10.1553179470'
host = 'www.utahrealestate.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

# myScraper = classes.scrappy(cookie,host,user_agent)

# collect all urls on all pages
# while myScraper.page <= 358:
#     print("page: " + myScraper.page) # just see progress as we go through all 356 pages
#     soup = myScraper.request_next_page()
#     myScraper.append_urls(soup)

myScraper = classes.scrappy(cookie, host, user_agent)

urls = []
with open('mls_urls.csv', newline='') as csvfile:
    urlreader = csv.reader(csvfile, delimiter=' ')
    for row in urlreader:
        urls.append(', '.join(row))

csv_file = open('mls_scrape2.csv', 'a')
csv_writer = csv.writer(csv_file)

i = 0
for url in urls[3100:len(urls)]:
    data = myScraper.scrape_report(url)
    csv_writer.writerow(data)
    i += 1
    if i%10 == 0:
        print(f'finished url # {i}')

# URLS = myScraper.urls

# print("printing urls to csv file")
# for url in URLS:
#     csv_writer.writerow(url)

# csv_file = open('mls_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(ROWS)

# once all urls are done then scrape each url and place data into csv
# URLS = myScraper.urls

# i = 0
# for url in URLS:
#     data = myScraper.scrape_report(url)
#     csv_writer.writerow(data)
#     if i%10 == 0:
#         print(i)
#     i += 1

csv_file.close()