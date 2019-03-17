from bs4 import BeautifulSoup
import requests
import csv

# with open('test_source.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

source = requests.get('https://www.utahrealestate.com/report/display/report/full/type/1/in_pop/1/listno/1586966/force//actor/').text

soup = BeautifulSoup(source, 'lxml')

print(soup)

mls_num = soup.div.find('h2', class_='mls-no').text
num_pictures = soup.find('span', class_='slide-of').text

# find table1
table1 = soup.find('table', class_='prop-overview-full').find_all('td')
list_price = table1[1].text
price_perANDoriginal_list_price = table1[5].text.strip()
status = table1[7].text
cdom = table1[9].text
list_date = table1[11].text
dom = table1[13].text
address = table1[15].text
area = table1[19].text
city = table1[21].text
county = table1[23].text
restrictions = table1[25].text
subdivision = table1[27].text
taxes = table1[31].text
zoning = table1[33].text
has_hoa = table1[35].text
hoa_transfer = table1[37].text
hoa_amenities = table1[43].text
pre_market = table1[45].text


DATA = [
    mls_num,
    num_pictures,

# table 1
    list_price,
    price_perANDoriginal_list_price,
    status,
    cdom,
    dom,
    address,
    city,
    county,
    subdivision,
    zoning,
    hoa_transfer,
    pre_market,
    status,
    list_date,
    area,
    restrictions,
    taxes,
    has_hoa,

    # school_dist,
    # elem,
    # jr_high,
    # sr_high,
    # other_school,

    # htype,
    # style,
    # year_built,
    # effect_yr_built,
    # deck_patio,
    # garage,
    # carport,
    # prkg_sp,
    # fin_bsmt,
    # bsmt,
    # garage_park,
    # driveway,
    # water,
    # water_shares,
    # spa,
    # community_pool,
    # master_level,
    # senior_comm,
    # animals,
    # const_status,
    # acres,
    # frontage,
    # side,
    # back,
    # irregular,

    # lvl4_sqfoot,
    # lvl4_bedrooms,
    # lvl4_bath_full,
    # lvl4_bath_three_fourth,
    # lvl4_bath_half,
    # lvl4_family,
    # lvl4_den,
    # lvl4_formal_living_room,
    # lvl4_kitchen_k,
    # lvl4_kitchen_b,
    # lvl4_kitchen_f,
    # lvl4_kitchen_s,
    # lvl4_laundry,
    # lvl4_fireplace,

    # lvl3_sqfoot,
    # lvl3_bedrooms,
    # lvl3_bath_full,
    # lvl3_bath_three_fourth,
    # lvl3_bath_half,
    # lvl3_family,
    # lvl3_den,
    # lvl3_formal_living_room,
    # lvl3_kitchen_k,
    # lvl3_kitchen_b,
    # lvl3_kitchen_f,
    # lvl3_kitchen_s,
    # lvl3_laundry,
    # lvl3_fireplace,
    
    # lvl2_sqfoot,
    # lvl2_bedrooms,
    # lvl2_bath_full,
    # lvl2_bath_three_fourth,
    # lvl2_bath_half,
    # lvl2_family,
    # lvl2_den,
    # lvl2_formal_living_room,
    # lvl2_kitchen_k,
    # lvl2_kitchen_b,
    # lvl2_kitchen_f,
    # lvl2_kitchen_s,
    # lvl2_laundry,
    # lvl2_fireplace,
    
    # lvl1_sqfoot,
    # lvl1_bedrooms,
    # lvl1_bath_full,
    # lvl1_bath_three_fourth,
    # lvl1_bath_half,
    # lvl1_family,
    # lvl1_den,
    # lvl1_formal_living_room,
    # lvl1_kitchen_k,
    # lvl1_kitchen_b,
    # lvl1_kitchen_f,
    # lvl1_kitchen_s,
    # lvl1_laundry,
    # lvl1_fireplace,
    
    # total_sqfoot,
    # total_bedrooms,
    # total_bath_full,
    # total_bath_three_fourth,
    # total_bath_half,
    # total_family,
    # total_den,
    # total_formal_living_room,
    # total_kitchen_k,
    # total_kitchen_b,
    # total_kitchen_f,
    # total_kitchen_s,
    # total_laundry,
    # total_fireplace,
    
    # roof,
    # heating,
    # air_cond,
    # floor,
    # window_cov,
    # has_pool,
    # pool_feat,
    # possession,
    # exterior,
    # has_solar,
    # landscape,
    # lot_facts,
    # exterior_feat,
    # interior_feat,
    # amenities,
    # inclusions,
    # terms,
    # storage,
    # access_feat,
    # utilities,
    # zoning,
    # remarks,
    # agt_remarks,
    # hoa_remarks,
    # show_inst,

    # owner,
    # owner_type,
    # contact,
    # contact_type,
    # bac,
    # dual_var,
    # list_type,
    # comm_type,
]

i  = 0 
for data in DATA:
    print(f'{i} {data}')
    i += 1
# csv_file.close()
