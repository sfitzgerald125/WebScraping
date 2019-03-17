import requests

s = requests.Session()
s.auth = ('fitspe','Fitz2L!fe;')
s.post('https://www.utahrealestate.com/auth/login/login_redirect//force_redirect/1')
print(s.auth)
context = s.get('https://www.utahrealestate.com/report/display/report/full/type/1/in_pop/1/listno/1505790/force//actor/')

print(context)