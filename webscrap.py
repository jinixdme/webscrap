import requests, bs4

def webscrap(url, *ids):
    values = []
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for id in ids:
        elems = soup.select("#" + id)
        values.append(int(elems[0].getText().replace(' ', '')))

    return values

# get burn - dead
result = webscrap('https://countrymeters.info/de/Germany', 'cp7', 'cp9')
print(result[0] - result[1])