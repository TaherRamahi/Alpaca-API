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
# $$$ This function allows us to buy shares with an  API call, we just input the arguments necessary in the function call and run the trade.py file in the terminal
def createOrder(symbol, qty, side, type, time_in_force):
    # the request to the API is going to be sent in a dict that i named data VID: 12.00
    data = {
    "symbol": symbol,
    "qty": qty,
    "side": side,
    "type": type ,
    "time_in_force": time_in_force


    }


    r = requests.post(ORDERS_URL, json = data, headers= HEADERS)
    
    return json.loads(r.content)

# $$$ we make requests such as this one bellow to buy/sell shares and the comments bellow can be used to make an order and we print the response to the terminal in the line under it.
# response = createOrder("AAPL", 100,"buy","market","gtc")
#print(response)

# This Function  serves to get all current orders from the API
def getOrders():
   r = requests.get(ORDERS_URL, headers= HEADERS)
   return json.loads(r.content)
# This below is actully running the get orders function and  printing to the terminal
ordersPending = getOrders()
print(ordersPending)

