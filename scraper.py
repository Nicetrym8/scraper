from bs4 import BeautifulSoup
import requests
from kithModel import kithModel

headers = {"""access-control-allow-method: GET
access-control-allow-origin: *
cache-control: max-age=900
content-encoding: gzip
content-security-policy: frame-ancestors 'self';
content-type: text/html; charset=UTF-8
date: Thu, 04 Aug 2022 18:16:01 GMT
expires: Thu, 04 Aug 2022 18:31:01 GMT
link: <https://food.fnr.sndimg.com>;rel="preconnect",<https://assets.adobedtm.com>;rel="preconnect",<https://cdns.gigya.com>;rel="preconnect",<https://code.adsales.snidigital.com>;rel="preconnect",<https://s.skimresources.com>;rel="preconnect",<https://www.player.video.snidigital.com>;rel="preconnect",<https://www.googletagservices.com>;rel="preconnect",<https://micro.rubiconproject.com>;rel="preconnect"
server: Apache
server-timing: origin; dur=220
server-timing: edge; dur=568
server-timing: cdn-cache; desc=REVALIDATE
set-cookie: layout=mobile
strict-transport-security: max-age=63072000; includeSubDomains
vary: User-Agent
vary: Accept-Encoding
x-akamai-transformed: 9 46881 0 pmb=mRUM,2"""

           }

session = requests.session()

response = session.get(
    "https://kith.com/collections/mens-footwear", headers=headers)

if response.status_code == 200:
    print("OK")
else:
    print("Error")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

for element in soup.find_all('li', class_='collection-product'):
    name = element.find('h1', class_="product-card__title").text.strip()
    price = element.find('span', class_="product-card__price").text.strip()
    link = "https://kith.com/" + element.find('a').get('href')

    product = kithModel(name, price, link)

    print(product.__repr__())
