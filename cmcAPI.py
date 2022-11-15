from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('apiKey')

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {

  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apiKey,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print("\033[32m############## All data ##############\033[0m")
  print(data)
  print("\033[32m#######################################\033[0m")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

# To write the data to the file, we just call the dump() function from json library
with open('response.json', 'w') as json_file:
    json.dump(data, json_file)

with open("response.json", "r") as f:
    my_dict = json.load(f)
    price = my_dict["data"][0]["quote"]["USD"]["price"]
    cmcRank = my_dict["data"][0]["cmc_rank"]

    print("\033[34m############## Specific data ##############\033[0m")
    print("\033[34mCurrent price: \033[0m", price)
    print("\033[34mCurrent cmc rank: \033[0m", cmcRank)
    print("\033[34m###########################################\033[0m")