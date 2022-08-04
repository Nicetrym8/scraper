import baseModel

# Aww my eyes. This is so wrong...


class kithModel(baseModel.BaseModel):
    pass

    def __init__(self):
        super().__init__(url="https://kith.com/collections/mens-footwear", headers={
            'authority': 'www.yeezysupply.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
            'sec-fetch-dest': 'document',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'accept-language': 'en-US,en;q=0.9',
        }
        )

    def parse(self):
        soup = super().parse()
        for element in soup.find_all('li', class_='collection-product'):
            name = element.find(
                'h1', class_="product-card__title").text.strip()
            link = "https://kith.com/" + element.find('a').get('href')

            self.result.append(baseModel.BaseObject(name, link).__repr__())
        return self.result
