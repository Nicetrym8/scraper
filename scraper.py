from models import *
models_list = [
    FoodNetworksModel(),
]
for el in models_list:
    print(str(el.parse()))
