import requests, json
from config import *


BASE_URL = "https://paper-api.alpaca.markets"

# we are using a placeholder "{}" and using the .format() to create a link that we can use to request data from our api.
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = { 'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY }

# This function returns the current acct info from the API
def getAcctInfo():
    #For this API we need to pass in our KEY and SECRET KEY when we attempt to make a call to the API using any URL. The KEY and SECRET key are passed into the header dict which I am still not sure how it works.
    r = requests.get(ACCOUNT_URL, headers= HEADERS)
    return json.loads(r.content)

#The args are all required by the API to create an order
def createOrder(symbol, qty, side, type, time_in_force):
    # the request to the API is going to be sent in a dict that i named data VID: 12.00
    data = {



    }


    r = requests.post(ORDERS_URL, headers= HEADERS)
    
    return json.loads(r.content)
        
