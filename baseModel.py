from abc import abstractclassmethod, abstractmethod
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

    def __init__(self, url, headers=None):
        self._url = url
        self._headers = headers

    def _request(self, url=""):
        if not url:
            url = self._url
        session = requests.session()
        response = session.get(
            url, headers=self._headers)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    @abstractmethod
    def parse(self):
        pass
