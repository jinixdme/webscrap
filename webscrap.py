import requests, bs4

res = requests.get('https://countrymeters.info/de/Germany')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

elems = soup.select('#cp7')
burn = int(elems[0].getText().replace(' ', ''))

elems = soup.select('#cp9')
dead = int(elems[0].getText().replace(' ', ''))

print(burn - dead)