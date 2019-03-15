from bs4 import BeautifulSoup
import requests
import csv

with open('test_source.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)

DATA = {
    'list_price': list_price,
    'price_per': price_per,
    'original_list_price': original_list_price,
    'cdom': cdom,
    'dom': dom,
    'address': address,
    'city': city,
    'county': county,
    'subdivision': subdivision,
    'tax_id': tax_id,
    'zoning': zoning,
    'hoa_transfer': hoa_transfer,
    'hoa_contact': hoa_contact,
    'hoa_ammenities': hoa_ammenities,
    'pre-market': pre-market,
    'tour_open': tour_open,
    'status': status,
    'list_date': list_date,
    'area': area,
    'restrictions': restrictions,
    'taxes': taxes,
    'hoa': hoa,

}
