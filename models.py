import baseModel
import string

# Aww my eyes. This is so wrong...


class FoodNetworksModel(baseModel.BaseModel):
    pass

    def __init__(self):
        super().__init__(url="https://www.foodnetwork.com/recipes/recipes-a-z")

    def __rough_parse(self):
        subroutes = ['123']  # + list(string.ascii_lowercase)
        rough_result = []
        for subroute in subroutes:
            soup = super()._request(self._url + '/' + subroute)

            for element in soup.find_all('li', class_='m-PromoList__a-ListItem'):
                rough_result.append('https:'+element.find('a').get('href'))
        return rough_result

    def parse(self):
        links_list = self.__rough_parse()
        for link in links_list:
            ingredients = []
            soup = super()._request(link)
            name = soup.find('meta', property="og:title")["content"]
            for element in soup.find_all('span', class_='o-Ingredients__a-Ingredient--CheckboxLabel'):
                ingredients.append(element.text)
            ingredients.pop(0)
            self.result.append(baseModel.BaseObject(
                name, ingredients).__repr__())
        return self.result
