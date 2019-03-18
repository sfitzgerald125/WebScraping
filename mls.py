from bs4 import BeautifulSoup
import requests
import csv

with open('test_source.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# source = requests.get('https://www.utahrealestate.com/report/display/report/full/type/1/in_pop/1/listno/1586966/force//actor/').text

# soup = BeautifulSoup(source, 'lxml')

mls_num = soup.div.find('h2', class_='mls-no').text

# find all td's
td = soup.find_all('td')
#start assigning vars
num_pictures = td[4].text
list_price = td[7].text
price_perANDoriginal_list_price = td[11].text.strip()
status = td[13].text

cdom = td[15].text
list_date = td[17].text
dom = td[19].text
address = td[21].text
area = td[25].text
city = td[27].text
county = td[29].text
restrictions = td[31].text
subdivision = td[33].text
taxes = td[35].text
zoning = td[39].text
has_hoa = td[41].text
hoa_transfer = td[43].text
hoa_amenities = td[49].text
pre_market = td[51].text
school_dist = td[53].text
elem = td[55].text
jr_high = td[57].text
sr_high = td[59].text
other_school = td[61].text

# home specs will be better to grab from separate var

htype = td[112].text
style = td[114].text
year_built = td[116].text.strip()
const_status = td[118].text
effect_yr_built = td[120].text
acres = td[122].text
deck_patio = td[124].text
frontage = td[126].text
garage = td[128].text
side = td[130].text
carport = td[132].text
back = td[134].text
prkg_sp = td[136].text
irregular = td[138].text
fin_bsmt = td[140].text

roof = td[144].text
bsmt = td[146].text
heating = td[148].text
garage_park = td[150].text
air_cond = td[152].text
driveway = td[154].text
floor = td[156].text
water = td[158].text
window_cov = td[160].text
water_shares = td[162].text
has_pool = td[164].text
has_spa = td[166].text
community_pool = td[166].text
pool_feat = td[168].text
master_level = td[170].text
possession = td[172].text
senior_comm = td[174].text
exterior = td[176].text
animals = td[178].text
has_solar = td[180].text
landscape = td[182].text
lot_facts = td[184].text
exterior_feat = td[186].text
interior_feat = td[188].text
amenities = td[190].text
inclusions = td[192].text
terms = td[194].text
storage = td[196].text
access_feat = td[198].text
utilities = td[200].text
zoning2 = td[202].text
remarks = td[204].text
agt_remarks = td[206].text
hoa_remarks = td[208].text
show_inst = td[210].text

owner = td[214].text
owner_type = td[216].text
contact = td[218].text
contact_type = td[220].text
bac = td[242].text
dual_var = td[244].text
list_type = td[246].text
comm_type = td[248].text
wthdrwn_dt = td[250].text
off_mkt_dt = td[252].text
exp_dt = td[254].text

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

    school_dist,
    elem,
    jr_high,
    sr_high,
    other_school,

    htype,
    style,
    year_built,
    effect_yr_built,
    deck_patio,
    garage,
    carport,
    prkg_sp,
    fin_bsmt,
    bsmt,
    garage_park,
    driveway,
    water,
    water_shares,
    spa,
    community_pool,
    master_level,
    senior_comm,
    animals,
    const_status,
    acres,
    frontage,
    side,
    back,
    irregular,
    
    roof,
    heating,
    air_cond,
    floor,
    window_cov,
    has_pool,
    pool_feat,
    possession,
    exterior,
    has_solar,
    landscape,
    lot_facts,
    exterior_feat,
    interior_feat,
    amenities,
    inclusions,
    terms,
    storage,
    access_feat,
    utilities,
    zoning,
    remarks,
    agt_remarks,
    hoa_remarks,
    show_inst,

    owner,
    owner_type,
    contact,
    contact_type,
    bac,
    dual_var,
    list_type,
    comm_type,

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
]

# csv_file.close()
