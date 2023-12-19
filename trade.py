import requests, json
from config import *


BASE_URL = "https://paper-api.alpaca.markets"

# we are using a placeholder "{}" and using the .format() to create a link that we can use to request data from our api.
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)

# This function returns the current acct info from the API
def getAcctInfo():
    #For this API we need to pass in our KEY and SECRET KEY when we attempt to make a call to the API using any URL. The KEY and SECRET key are passed into the header dict which I am still not sure how it works.
    r = requests.get(ACCOUNT_URL, headers={ 'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY })
    return json.loads(r.content)

