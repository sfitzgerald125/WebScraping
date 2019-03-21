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

cookie = '__utmc=41202813; __utmz=41202813.1553106212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ureBrowserSession=1553123150368895489500; _gcl_au=1.1.1217016442.1553123151; __utma=41202813.623660756.1553106212.1553116294.1553123151.3; __gads=ID=2c13cb39f6d4b3b5:T=1553123150:S=ALNI_MY5y4hpO7v9WKtYXQaelQ9cTbj0pA; _ga=GA1.2.623660756.1553106212; _gid=GA1.2.2135618890.1553123153; __qca=P0-1804500325-1553123154710; OX_plg=pm; ureServerSession=1553123150368895489500; PHPSESSID=j93697h1k28f4l1c9b2oj5gai2; btpdb.6EeDEhH.dGZjLjQ4NTE4NA=UkVRVUVTVFMuMTI; HELP_RIGHTS=1; __utmv=41202813.Member; __utmt=1; __utmb=41202813.24.10.1553123151'
host = 'www.utahrealestate.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

myScraper = classes.scrappy(cookie,host,user_agent)

# collect all urls on page 1
soup = myScraper.request_next_page(myScraper.page)
# turn page
myScraper.append_urls(soup)

# once all urls are done then scrape each url
URLS = myScraper.urls
for url in URLS:
    data = myScraper.scrape_report(url)




# while myScraper.next_page <= 2:


# DATA = myScraper.scrape_report(soup)

# csv_file = open('mls_scrape.csv', 'a')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(scrape.ROWS)
# csv_writer.writerow(DATA)
# csv_file.close()