from bs4 import BeautifulSoup
import requests


class BaseObject:
    name = str
    ingredients = list

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return self.__dict__


class BaseModel:
    result = []
    headers = dict
    url = str

    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    def __request(self, url=""):
        if not url:
            url = self.url
        session = requests.session()
        response = session.get(
            url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def parse(self, url=""):
        return self.__request(url)
