import requests
BASE_URL = "https://paper-api.alpaca.markets"

r = request.get(BASE_URL)

print(r.content)