from bs4 import BeautifulSoup
import re
import requests
import csv

with open('test4.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# start assigning vars
mls_num = soup.find('h2', class_='mls-no').text
num_pictures = soup.find('span', class_='slide-of').text

# table1 vars
table1 = soup.find('table', class_="prop-overview-full")
list_price = table1.find(onclick=re.compile("displayMortgageCalculator")).text
price_perANDoriginal_list_price = table1.find(string=re.compile('Price Per:')).find_next('td').text.strip()
status = table1.find(string=re.compile("^Status:")).find_next('td').text
cdom = table1.find(string=re.compile("^CDOM:")).find_next('td').text
list_date = table1.find(string=re.compile("List Date:")).find_next("td").text
dom = table1.find(string=re.compile("^DOM:")).find_next("td").text
address = table1.find(string=re.compile("^Address:")).find_next("td").text
area = table1.find(string=re.compile("Area:")).find_next("td").text
city = table1.find(string=re.compile("^City:")).find_next("td").text
county = table1.find(string=re.compile("County:")).find_next("td").text
restrictions = table1.find(string=re.compile("Restrictions:")).find_next("td").text
subdivision = table1.find(string=re.compile("Proj/Subdiv")).find_next("td").text
taxes = table1.find(string=re.compile("Taxes:")).find_next("td").text
zoning1 = table1.find(string=re.compile("Zoning")).find_next("td").text
has_hoa = table1.find(string=re.compile("HOA")).find_next("td").text
hoa_transfer = table1.find(string=re.compile("HOA Transfer:")).find_next("td").text
hoa_amenities = table1.find(string=re.compile("HOA Amenities")).find_next("td").text
pre_market = table1.find(string=re.compile("Pre-Market")).find_next("td").text

# table2 vars
table2 = table1.find_next('table')
school_dist = table2.find(string=re.compile("School Dist:")).find_next("td").text
elem = table2.find(string=re.compile("Elem:")).find_next("td").text
jr_high = table2.find(string=re.compile("Jr High:")).find_next("td").text
sr_high = table2.find(string=re.compile("Sr High:")).find_next("td").text

#table3 vars
table3 = table2.find_next('table')
td_finder = table3.find(string=re.compile("Tot"))

total_sqfoot = td_finder.find_next("td")
total_bedrooms = total_sqfoot.find_next("td")
total_bath_full = total_bedrooms.find_next("td")
total_bath_three_fourth = total_bath_full.find_next("td")
total_bath_half = total_bath_three_fourth.find_next("td")
total_family = total_bath_half.find_next("td")
total_den = total_family.find_next("td")
total_formal_living_room = total_den.find_next("td")
total_kitchen_k = total_formal_living_room.find_next("td")
total_kitchen_b = total_kitchen_k.find_next("td")
total_kitchen_f = total_kitchen_b.find_next("td")
total_kitchen_s = total_kitchen_f.find_next("td")
total_laundry = total_kitchen_s.find_next("td")
total_fireplace = total_laundry.find_next("td")



print(total_fireplace)
# .find_next("td")


# htype = td[112].text
# style = td[114].text
# year_built = td[116].text.strip()
# const_status = td[118].text
# effect_yr_built = td[120].text
# acres = td[122].text
# deck_patio = td[124].text
# frontage = td[126].text
# garage = td[128].text
# side = td[130].text
# carport = td[132].text
# back = td[134].text
# prkg_sp = td[136].text
# irregular = td[138].text
# fin_bsmt = td[140].text

# roof = td[144].text
# bsmt = td[146].text
# heating = td[148].text
# garage_park = td[150].text
# air_cond = td[152].text
# driveway = td[154].text
# floor = td[156].text
# water = td[158].text
# window_cov = td[160].text
# water_shares = td[162].text
# has_pool = td[164].text
# has_spa = td[166].text
# community_pool = td[166].text
# pool_feat = td[168].text
# master_level = td[170].text
# possession = td[172].text
# senior_comm = td[174].text
# exterior = td[176].text
# animals = td[178].text
# has_solar = td[180].text
# landscape = td[182].text
# lot_facts = td[184].text
# exterior_feat = td[186].text
# interior_feat = td[188].text
# amenities = td[190].text
# inclusions = td[192].text
# terms = td[194].text
# storage = td[196].text
# access_feat = td[198].text
# utilities = td[200].text
# zoning2 = td[202].text
# remarks = td[204].text
# agt_remarks = td[206].text
# hoa_remarks = td[208].text
# show_inst = td[210].text

# owner = td[214].text
# owner_type = td[216].text
# contact = td[218].text
# contact_type = td[220].text
# bac = td[242].text
# dual_var = td[244].text
# list_type = td[246].text
# comm_type = td[248].text
# wthdrwn_dt = td[250].text
# off_mkt_dt = td[252].text
# exp_dt = td[254].text

DATA = [
    mls_num,
    num_pictures,
    list_price,
    price_perANDoriginal_list_price,
    status,
    cdom,
    list_date,
    dom,
    address,
    area,
    city,
    county,
    restrictions,
    subdivision,
    taxes,
    zoning1,
    has_hoa,
    hoa_transfer,
    hoa_amenities,
    pre_market,
    # school_dist,
    # elem,
    # jr_high,
    # sr_high,
    # other_school,
    # htype,
    # style,
    # year_built,
    # const_status,
    # effect_yr_built,
    # acres,
    # deck_patio,
    # frontage,
    # garage,
    # side,
    # carport,
    # back,
    # prkg_sp,
    # irregular,
    # fin_bsmt,
    # roof,
    # bsmt,
    # heating,
    # garage_park,
    # air_cond,
    # driveway,
    # floor,
    # water,
    # window_cov,
    # water_shares,
    # has_pool,
    # has_spa,
    # community_pool,
    # pool_feat,
    # master_level,
    # possession,
    # senior_comm,
    # exterior,
    # animals,
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
    # zoning2,
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
    # wthdrwn_dt,
    # off_mkt_dt,
    # exp_dt,

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
]

# for data in DATA:
#     print(data)
# csv_writer.writerow(DATA)

# csv_file.close()