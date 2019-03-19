from bs4 import BeautifulSoup
import re
import requests
import csv

with open('test3.html') as html_file:
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

# table4 vars
table4 = table3.find_next('table').find_next("table")
htype = table4.find(string=re.compile("Type:")).find_next("td").text
style = table4.find(string=re.compile("Style")).find_next("td").text
year_built = table4.find(string=re.compile("Year Built:")).find_next("td").text.strip()
const_status = table4.find(string=re.compile("Const Status:")).find_next("td").text.strip()
effect_yr_built = table4.find(string=re.compile("Effect Yr Blt:")).find_next("td").text
acres = table4.find(string=re.compile("Acres:")).find_next("td").text
deck_patio = table4.find(string=re.compile("Deck")).find_next("td").text
frontage = table4.find(string=re.compile("Frontage:")).find_next("td").text
garage = table4.find(string=re.compile("Garage:")).find_next("td").text
side = table4.find(string=re.compile("Side:")).find_next("td").text
carport = table4.find(string=re.compile("Carport")).find_next("td").text
back = table4.find(string=re.compile("Back:")).find_next("td").text
prkg_sp = table4.find(string=re.compile("Prkg Sp")).find_next("td").text
irregular = table4.find(string=re.compile("Irregular")).find_next("td").text
fin_bsmt = table4.find(string=re.compile("Fin Bsmt")).find_next("td").text

# table5 vars
table5 = table4.find_next("table")
roof = table5.find(string=re.compile("Roof:")).find_next("td").text
bsmt = table5.find(string=re.compile("Basement:")).find_next("td").text
heating = table5.find(string=re.compile("Heating:")).find_next("td").text
garage_park = table5.find(string=re.compile("Garage/Park:")).find_next("td").text
air_cond = table5.find(string=re.compile("Air Cond:")).find_next("td").text
driveway = table5.find(string=re.compile("Driveway:")).find_next("td").text
floor = table5.find(string=re.compile("Floor:")).find_next("td").text
water = table5.find(string=re.compile("Water:")).find_next("td").text
window_cov = table5.find(string=re.compile("Window Cov:")).find_next("td").text
water_shares = table5.find(string=re.compile("Water Shares:")).find_next("td").text
has_pool = table5.find(string=re.compile("Pool\?")).find_next("td").text
has_spa = table5.find(string=re.compile("Spa\?")).find_next("td").text
community_pool = table5.find(string=re.compile("Community Pool\?")).find_next("td").text
pool_feat = table5.find(string=re.compile("Pool Feat:")).find_next("td").text
master_level = table5.find(string=re.compile("Master Level:")).find_next("td").text
possession = table5.find(string=re.compile("Possession")).find_next("td").text
senior_comm = table5.find(string=re.compile("Senior Comm:")).find_next("td").text
exterior = table5.find(string=re.compile("Exterior")).find_next("td").text
animals = table5.find(string=re.compile("Animals:")).find_next("td").text
has_solar = table5.find(string=re.compile("Has Solar\?")).find_next("td").text

# table6 vars
table6 = table5.find_next("table")
landscape = table6.find(string=re.compile("Landscape")).find_next("td").text
lot_facts = table6.find(string=re.compile("Lot Facts")).find_next("td").text
exterior_feat = table6.find(string=re.compile("Exterior Feat:")).find_next("td").text
interior_feat = table6.find(string=re.compile("Interior Feat:")).find_next("td").text
amenities = table6.find(string=re.compile("Amenities:")).find_next("td").text
inclusions = table6.find(string=re.compile("Inclusions")).find_next("td").text
terms = table6.find(string=re.compile("Terms")).find_next("td").text
storage = table6.find(string=re.compile("Storage")).find_next("td").text
access_feat = table6.find(string=re.compile("Access Feat:")).find_next("td").text
utilities = table6.find(string=re.compile("Utilities")).find_next("td").text
zoning2 = table6.find(string=re.compile("Zoning:")).find_next("td").text
remarks = table6.find(string=re.compile("Remarks")).find_next("td").text
agt_remarks = table6.find(string=re.compile("Agt Remarks:")).find_next("td").text

# table7 vars
table7 = table6.find_next("table")
show_inst = table7.find(string=re.compile("Show Inst:")).find_next("td").text
owner = table7.find(string=re.compile("Owner")).find_next("td").text
owner_type = table7.find(string=re.compile("Owner Type:")).find_next("td").text
contact = table7.find(string=re.compile("Contact:")).find_next("td").text
contact_type = table7.find(string=re.compile("Contact Type:")).find_next("td").text
l_agent = table7.find(string=re.compile("L.Agent")).find_next("td").text
l_office = table7.find(string=re.compile("L.Office:")).find_next("td").text
l_broker = table7.find(string=re.compile("L.Broker")).find_next("td").text

# table8 vars
table8 = table7.find_next("table")
bac = table8.find(string=re.compile("BAC:")).find_next("td").text
dual_var = table8.find(string=re.compile("Dual.Var:")).find_next("td").text
list_type = table8.find(string=re.compile("List Type:")).find_next("td").text
comm_type = table8.find(string=re.compile("Comm Type:")).find_next("td").text
wthdrwn_dt = table8.find(string=re.compile("Wthdrwn Dt:")).find_next("td").text
off_mkt_dt = table8.find(string=re.compile("Off Mkt Dt:")).find_next("td").text
exp_dt = table8.find(string=re.compile("Exp Dt:")).find_next("td").text


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

    school_dist,
    elem,
    jr_high,
    sr_high,

    total_sqfoot.text,
    total_bedrooms.text,
    total_bath_full.text,
    total_bath_three_fourth.text,
    total_bath_half.text,
    total_family.text,
    total_den.text,
    total_formal_living_room.text,
    total_kitchen_k.text,
    total_kitchen_b.text,
    total_kitchen_f.text,
    total_kitchen_s.text,
    total_laundry.text,
    total_fireplace.text,

    htype,
    style,
    year_built,
    const_status,
    effect_yr_built,
    acres,
    deck_patio,
    frontage,
    garage,
    side,
    carport,
    back,
    prkg_sp,
    irregular,
    fin_bsmt,

    roof,
    bsmt,
    heating,
    garage_park,
    air_cond,
    driveway,
    floor,
    water,
    window_cov,
    water_shares,
    has_pool,
    has_spa,
    community_pool,
    pool_feat,
    master_level,
    possession,
    senior_comm,
    exterior,
    animals,
    has_solar,

    landscape,
    lot_facts,
    inclusions,
    terms,
    storage,
    utilities,
    zoning2,
    remarks,
    exterior_feat,
    interior_feat,
    amenities,
    access_feat,
    agt_remarks,



    show_inst,
    owner,
    owner_type,
    contact,
    contact_type,
    l_agent,
    l_office,
    l_broker,

    bac,
    dual_var,
    list_type,
    comm_type,
    wthdrwn_dt,
    off_mkt_dt,
    exp_dt,
]

for data in DATA:
    print(data)
# csv_writer.writerow(DATA)

# csv_file.close()