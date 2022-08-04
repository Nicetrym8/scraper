from models import *
data = []
models_list = [
    kithModel(),
]
for el in models_list:
    print(str(el.parse()))
