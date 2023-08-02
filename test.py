import requests
import json

url = "https://www.avito.ru/"
response = requests.get(url)

body_dict = response.json()

print(body_dict)