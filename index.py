import requests
page = requests.get('http://example.com')
contents = page.content

print(contents)

