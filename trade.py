import requests
from config import *
BASE_URL = "https://paper-api.alpaca.markets"

r = requests.get(BASE_URL)

print(r.content)