class BaseModel:
    name = str
    link = str
    header = list

    def __init__(self, name, price, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return str(self.__dict__)
