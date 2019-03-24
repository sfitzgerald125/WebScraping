from bs4 import BeautifulSoup
import re
import requests

class scrappy:
    HEADERS = {}
    urls = []
    page = 1 # set to page 1 for the start

    def __init__(self, cookie, host, user_agent):
        self.HEADERS['Cookie'] = cookie
        self.HEADERS['Host'] = host
        self.HEADERS['User-Agent'] = user_agent
    
    def request_next_page(self):
        with requests.Session() as s:
            url = f'https://www.utahrealestate.com/search/perform/md/3ff38b95fd89a31bdd1a02d886df8a88/recent/1?page={self.page}'
            r = s.get(url, headers=self.HEADERS)
            soup = BeautifulSoup(r.content, 'lxml')
            self.page += 1
        return soup

    def append_urls(self, soup):        
        table = soup.find("table", class_="datatable")
        a_tags = table.find_all("a", title=re.compile("View property history"))

        for a in a_tags:
            a = a['href']
            a = f'https://www.utahrealestate.com{a}'
            self.urls.append(a)
        
    def scrape_report(self, url):
        with requests.Session() as s:
            r = s.get(url, headers=self.HEADERS)
            soup = BeautifulSoup(r.content, 'lxml')

        # start assigning vars
        default_value = "NULL"
        try:
            mls_num = soup.find('h2', class_='mls-no').text
        except Exception as e:
            mls_num = default_value

        try:
            num_pictures = soup.find('span', class_='slide-of').text
        except Exception as e:
            num_pictures = default_value

        # table1 vars
        table1 = soup.find('table', class_="prop-overview-full")
        try:
            list_price = table1.find(onclick=re.compile("displayMortgageCalculator")).text
        except Exception as e:
            list_price = default_value    

        try:
            price_perANDoriginal_list_price = table1.find(string=re.compile('Price Per:')).find_next('td').text.strip()
        except Exception as e:
            price_perANDoriginal_list_price = default_value

        try:
            status = table1.find(string=re.compile("^Status:")).find_next('td').text
        except Exception as e:
            status = default_value

        try:
            cdom = table1.find(string=re.compile("^CDOM:")).find_next('td').text
        except Exception as e:
            cdom = default_value

        try:
            list_date = table1.find(string=re.compile("List Date:")).find_next("td").text
        except Exception as e:
            list_date = default_value

        try:
            dom = table1.find(string=re.compile("^DOM:")).find_next("td").text
        except Exception as e:
            dom = default_value

        try:
            address = table1.find(string=re.compile("^Address:")).find_next("td").text
        except Exception as e:
            address = default_value

        try:
            area = table1.find(string=re.compile("Area:")).find_next("td").text
        except Exception as e:
            area = default_value

        try:
            city = table1.find(string=re.compile("^City:")).find_next("td").text
        except Exception as e:
            city = default_value

        try:
            county = table1.find(string=re.compile("County:")).find_next("td").text
        except Exception as e:
            county = default_value

        try:
            restrictions = table1.find(string=re.compile("Restrictions:")).find_next("td").text
        except Exception as e:
            restrictions = default_value

        try:
            subdivision = table1.find(string=re.compile("Proj/Subdiv")).find_next("td").text
        except Exception as e:
            subdivision = default_value

        try:
            taxes = table1.find(string=re.compile("Taxes:")).find_next("td").text
        except Exception as e:
            taxes = default_value

        try:
            zoning1 = table1.find(string=re.compile("Zoning")).find_next("td").text
        except Exception as e:
            zoning1 = default_value

        try:
            has_hoa = table1.find(string=re.compile("HOA")).find_next("td").text
        except Exception as e:
            has_hoa = default_value

        try:
            hoa_transfer = table1.find(string=re.compile("HOA Transfer:")).find_next("td").text
        except Exception as e:
            hoa_transfer = default_value

        try:
            hoa_amenities = table1.find(string=re.compile("HOA Amenities")).find_next("td").text
        except Exception as e:
            hoa_amenities = default_value

        try:
            pre_market = table1.find(string=re.compile("Pre-Market")).find_next("td").text
        except Exception as e:
            pre_market = default_value    

        # table2 vars
        table2 = table1.find_next('table')
        try:
            school_dist = table2.find(string=re.compile("School Dist:")).find_next("td").text
        except Exception as e:
            school_dist = default_value
        try:
            elem = table2.find(string=re.compile("Elem:")).find_next("td").text
        except Exception as e:
            elem = default_value
        try:
            jr_high = table2.find(string=re.compile("Jr High:")).find_next("td").text
        except Exception as e:
            jr_high = default_value
        try:
            sr_high = table2.find(string=re.compile("Sr High:")).find_next("td").text
        except Exception as e:
            sr_high = default_value

        #table3 vars    
        table3 = table2.find_next('table')    
        td_finder = table3.find(string=re.compile("Tot"))

        try:
            total_sqfoot = td_finder.find_next("td")
        except Exception as e:
            total_sqfoot = default_value

        try:
            total_bedrooms = total_sqfoot.find_next("td")
        except Exception as e:
            total_bedrooms = default_value

        try:
            total_bath_full = total_bedrooms.find_next("td")
        except Exception as e:
            total_bath_full = default_value

        try:
            total_bath_three_fourth = total_bath_full.find_next("td")
        except Exception as e:
            total_bath_three_fourth = default_value

        try:
            total_bath_half = total_bath_three_fourth.find_next("td")
        except Exception as e:
            total_bath_half = default_value

        try:
            total_family = total_bath_half.find_next("td")
        except Exception as e:
            total_family = default_value

        try:
            total_den = total_family.find_next("td")
        except Exception as e:
            total_den = default_value

        try:
            total_formal_living_room = total_den.find_next("td")
        except Exception as e:
            total_formal_living_room = default_value

        try:
            total_kitchen_k = total_formal_living_room.find_next("td")
        except Exception as e:
            total_kitchen_k = default_value

        try:
            total_kitchen_b = total_kitchen_k.find_next("td")
        except Exception as e:
            total_kitchen_b = default_value

        try:
            total_kitchen_f = total_kitchen_b.find_next("td")
        except Exception as e:
            total_kitchen_f = default_value

        try:
            total_kitchen_s = total_kitchen_f.find_next("td")
        except Exception as e:
            total_kitchen_s = default_value

        try:
            total_laundry = total_kitchen_s.find_next("td")
        except Exception as e:
            total_laundry = default_value

        try:
            total_fireplace = total_laundry.find_next("td")
        except Exception as e:
            total_fireplace = default_value

        # table4 vars
        table4 = table3.find_next('table').find_next("table")
        try:
            htype = table4.find(string=re.compile("Type:")).find_next("td").text
        except Exception as e:
            htype = default_value

        try:
            style = table4.find(string=re.compile("Style")).find_next("td").text
        except Exception as e:
            style = default_value

        try:
            year_built = table4.find(string=re.compile("Year Built:")).find_next("td").text.strip()
        except Exception as e:
            year_built = default_value

        try:
            const_status = table4.find(string=re.compile("Const Status:")).find_next("td").text.strip()
        except Exception as e:
            const_status = default_value

        try:
            effect_yr_built = table4.find(string=re.compile("Effect Yr Blt:")).find_next("td").text
        except Exception as e:
            effect_yr_built = default_value

        try:
            acres = table4.find(string=re.compile("Acres:")).find_next("td").text
        except Exception as e:
            acres = default_value

        try:
            deck_patio = table4.find(string=re.compile("Deck")).find_next("td").text
        except Exception as e:
            deck_patio = default_value

        try:
            frontage = table4.find(string=re.compile("Frontage:")).find_next("td").text
        except Exception as e:
            frontage = default_value

        try:
            garage = table4.find(string=re.compile("Garage:")).find_next("td").text
        except Exception as e:
            garage = default_value

        try:
            side = table4.find(string=re.compile("Side:")).find_next("td").text
        except Exception as e:
            side = default_value

        try:
            carport = table4.find(string=re.compile("Carport")).find_next("td").text
        except Exception as e:
            carport = default_value

        try:
            back = table4.find(string=re.compile("Back:")).find_next("td").text
        except Exception as e:
            back = default_value

        try:
            prkg_sp = table4.find(string=re.compile("Prkg Sp")).find_next("td").text
        except Exception as e:
            prkg_sp = default_value

        try:
            irregular = table4.find(string=re.compile("Irregular")).find_next("td").text
        except Exception as e:
            irregular = default_value

        try:
            fin_bsmt = table4.find(string=re.compile("Fin Bsmt")).find_next("td").text
        except Exception as e:
            fin_bsmt = default_value

        # table5 vars
        table5 = table4.find_next("table")
        try:
            roof = table5.find(string=re.compile("Roof:")).find_next("td").text
        except Exception as e:
            roof = default_value

        try:
            bsmt = table5.find(string=re.compile("Basement:")).find_next("td").text
        except Exception as e:
            bsmt = default_value

        try:
            heating = table5.find(string=re.compile("Heating:")).find_next("td").text
        except Exception as e:
            heating = default_value

        try:
            garage_park = table5.find(string=re.compile("Garage/Park:")).find_next("td").text
        except Exception as e:
            garage_park = default_value

        try:
            air_cond = table5.find(string=re.compile("Air Cond:")).find_next("td").text
        except Exception as e:
            air_cond = default_value

        try:
            driveway = table5.find(string=re.compile("Driveway:")).find_next("td").text
        except Exception as e:
            driveway = default_value

        try:
            floor = table5.find(string=re.compile("Floor:")).find_next("td").text
        except Exception as e:
            floor = default_value

        try:
            water = table5.find(string=re.compile("Water:")).find_next("td").text
        except Exception as e:
            water = default_value

        try:
            window_cov = table5.find(string=re.compile("Window Cov:")).find_next("td").text
        except Exception as e:
            window_cov = default_value

        try:
            water_shares = table5.find(string=re.compile("Water Shares:")).find_next("td").text
        except Exception as e:
            water_shares = default_value

        try:
            has_pool = table5.find(string=re.compile("Pool\?")).find_next("td").text
        except Exception as e:
            has_pool = default_value

        try:
            has_spa = table5.find(string=re.compile("Spa\?")).find_next("td").text
        except Exception as e:
            has_spa = default_value

        try:
            community_pool = table5.find(string=re.compile("Community Pool\?")).find_next("td").text
        except Exception as e:
            community_pool = default_value

        try:
            pool_feat = table5.find(string=re.compile("Pool Feat:")).find_next("td").text
        except Exception as e:
            pool_feat = default_value

        try:
            master_level = table5.find(string=re.compile("Master Level:")).find_next("td").text
        except Exception as e:
            master_level = default_value

        try:
            possession = table5.find(string=re.compile("Possession")).find_next("td").text
        except Exception as e:
            possession = default_value

        try:
            senior_comm = table5.find(string=re.compile("Senior Comm:")).find_next("td").text
        except Exception as e:
            senior_comm = default_value

        try:
            exterior = table5.find(string=re.compile("Exterior")).find_next("td").text
        except Exception as e:
            exterior = default_value

        try:
            animals = table5.find(string=re.compile("Animals:")).find_next("td").text
        except Exception as e:
            animals = default_value

        try:
            has_solar = table5.find(string=re.compile("Has Solar\?")).find_next("td").text
        except Exception as e:
            has_solar = default_value

        # table6 vars
        table6 = table5.find_next("table")
        try:
            landscape = table6.find(string=re.compile("Landscape")).find_next("td").text
        except Exception as e:
            landscape = default_value

        try:
            lot_facts = table6.find(string=re.compile("Lot Facts")).find_next("td").text
        except Exception as e:
            lot_facts = default_value

        try:
            exterior_feat = table6.find(string=re.compile("Exterior Feat:")).find_next("td").text
        except Exception as e:
            exterior_feat = default_value

        try:
            interior_feat = table6.find(string=re.compile("Interior Feat:")).find_next("td").text
        except Exception as e:
            interior_feat = default_value

        try:
            amenities = table6.find(string=re.compile("Amenities:")).find_next("td").text
        except Exception as e:
            amenities = default_value

        try:
            inclusions = table6.find(string=re.compile("Inclusions")).find_next("td").text
        except Exception as e:
            inclusions = default_value

        try:
            terms = table6.find(string=re.compile("Terms")).find_next("td").text
        except Exception as e:
            terms = default_value

        try:
            storage = table6.find(string=re.compile("Storage")).find_next("td").text
        except Exception as e:
            storage = default_value

        try:
            access_feat = table6.find(string=re.compile("Access Feat:")).find_next("td").text
        except Exception as e:
            access_feat = default_value

        try:
            utilities = table6.find(string=re.compile("Utilities")).find_next("td").text
        except Exception as e:
            utilities = default_value

        try:
            zoning2 = table6.find(string=re.compile("Zoning:")).find_next("td").text
        except Exception as e:
            zoning2 = default_value

        try:
            remarks = table6.find(string=re.compile("Remarks")).find_next("td").text
        except Exception as e:
            remarks = default_value

        try:
            agt_remarks = table6.find(string=re.compile("Agt Remarks:")).find_next("td").text
        except Exception as e:
            agt_remarks = default_value
            
        # table7 vars
        try:
            table7 = table6.find_next("table")
        except Exception as e:
            table7 = default_value

        try:
            show_inst = table7.find(string=re.compile("Show Inst:")).find_next("td").text
        except Exception as e:
            show_inst = default_value

        try:
            owner = table7.find(string=re.compile("Owner")).find_next("td").text
        except Exception as e:
            owner = default_value

        try:
            owner_type = table7.find(string=re.compile("Owner Type:")).find_next("td").text
        except Exception as e:
            owner_type = default_value

        try:
            contact = table7.find(string=re.compile("Contact:")).find_next("td").text
        except Exception as e:
            contact = default_value

        try:
            contact_type = table7.find(string=re.compile("Contact Type:")).find_next("td").text
        except Exception as e:
            contact_type = default_value

        try:
            l_agent = table7.find(string=re.compile("L.Agent")).find_next("td").text
        except Exception as e:
            l_agent = default_value

        try:
            l_office = table7.find(string=re.compile("L.Office:")).find_next("td").text
        except Exception as e:
            l_office = default_value

        try:
            l_broker = table7.find(string=re.compile("L.Broker")).find_next("td").text
        except Exception as e:
            l_broker = default_value

        # table8 vars
        try:
            table8 = table7.find_next("table")
        except Exception as e:
            table8 = default_value
            
        try:
            bac = table8.find(string=re.compile("BAC:")).find_next("td").text
        except Exception as e:
            bac = default_value

        try:
            dual_var = table8.find(string=re.compile("Dual.Var:")).find_next("td").text
        except Exception as e:
            dual_var = default_value

        try:
            list_type = table8.find(string=re.compile("List Type:")).find_next("td").text
        except Exception as e:
            list_type = default_value

        try:
            comm_type = table8.find(string=re.compile("Comm Type:")).find_next("td").text
        except Exception as e:
            comm_type = default_value

        try:
            wthdrwn_dt = table8.find(string=re.compile("Wthdrwn Dt:")).find_next("td").text
        except Exception as e:
            wthdrwn_dt = default_value

        try:
            off_mkt_dt = table8.find(string=re.compile("Off Mkt Dt:")).find_next("td").text
        except Exception as e:
            off_mkt_dt = default_value

        try:
            exp_dt = table8.find(string=re.compile("Exp Dt:")).find_next("td").text
        except Exception as e:
            exp_dt = default_value

        DATA = [
            # table 1
            mls_num, num_pictures, list_price, price_perANDoriginal_list_price, status, cdom, list_date, dom, address, area, 
            city, county, restrictions, subdivision, taxes, zoning1, has_hoa, hoa_transfer, hoa_amenities, pre_market,
            # table 2
            school_dist, elem, jr_high, sr_high,
            # table 3
            total_sqfoot.text, total_bedrooms.text, total_bath_full.text, total_bath_three_fourth.text, total_bath_half.text, 
            total_family.text, total_den.text, total_formal_living_room.text, total_kitchen_k.text, total_kitchen_b.text, 
            total_kitchen_f.text, total_kitchen_s.text, total_laundry.text, total_fireplace.text,
            # table 4
            htype, style, year_built, const_status, effect_yr_built, acres, deck_patio, frontage, garage, side, carport, back, 
            prkg_sp, irregular, fin_bsmt,
            # table 5
            roof, bsmt, heating, garage_park, air_cond, driveway, floor, water, window_cov, water_shares, has_pool, has_spa, 
            community_pool, pool_feat, master_level, possession, senior_comm, exterior, animals, has_solar,
            # table 6
            landscape, lot_facts, inclusions, terms, storage, utilities, zoning2, remarks, exterior_feat, interior_feat, 
            amenities, access_feat, agt_remarks,
            # table 7
            show_inst, owner, owner_type, contact, contact_type, l_agent, l_office, l_broker,
            # table 8
            bac, dual_var, list_type, comm_type, wthdrwn_dt, off_mkt_dt, exp_dt,
        ]

        return DATA