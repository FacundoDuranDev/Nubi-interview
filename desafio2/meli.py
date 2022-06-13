import os
import requests
from datetime import date
import json
import re

sesion = requests.session()
directorio = os.getcwd() + "/search" + "json" + date.today().strftime("%Y%m")
if not os.path.exists(directorio):
    os.makedirs(directorio)
categoria = sesion.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1403').json()
print(categoria)
file = open(directorio
            + "/"
            + categoria['filters'][0]['values'][0]['id']
            + ".json", 'w+')
file.write(json.dumps(categoria))
