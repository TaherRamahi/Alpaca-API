import requests
from config import *
BASE_URL = "https://paper-api.alpaca.markets"


#This is to see acct info we are using a placeholder and using the .format() to create a link that we can use to request acct data. VID 8:42
Acount_URL = "{}/v2/account".format(BASE_URL)
acctInfo = requests.get(Acount_URL)

#For this API we need to pass in our KEY and SECRET KEY when we attempt to make a call to the API using any URL. The KEY and SaECRET key are passed into the header dict which I am still not sure how it works.
r = requests.get(Acount_URL, headers={ 'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY })

print(r.content)