from bs4 import BeautifulSoup
import requests


class BaseObject:
    name = str
    link = str

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return self.__dict__


class BaseModel:
    result = []
    headers = dict
    url = str

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __request(self):
        session = requests.session()
        response = session.get(
            self.url, headers=self.headers)

        if response.status_code == 200:
            print("OK")
        else:
            print("Error")
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def parse(self):
        return self.__request()
