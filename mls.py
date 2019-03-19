from bs4 import BeautifulSoup
import requests
import csv
import data

with open('test3.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

ROWS = []

DATA = data.set_variables(soup)
    
for data in DATA:
    print(data)

# csv_writer.writerow(DATA)

# csv_file.close()