from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
load_dotenv()

apiKey = os.getenv('apiKey')
coin = 0
current_coin = 0
amount_of_coins = 5

for i in range (amount_of_coins):
  current_coin += 1;
  # Generates output of coin 1
  if current_coin == 1:
    coin = 1
  # Generates output of coin 2
  elif current_coin == 2:
    coin = 2
  # Generates output of coin 3
  elif current_coin == 3:
    coin = 3
  # Generates output of coin 4
  elif current_coin == 4:
    coin = 4
  # Generates output of coin 5
  elif current_coin == 5:
    coin = 10
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':coin,
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
      # Saves better variables
      if current_coin == 1:
        coin1_price = my_dict["data"][0]["quote"]["USD"]["price"]
        coin1_cmcRank = my_dict["data"][0]["cmc_rank"]
      elif current_coin == 2:
        coin2_price = my_dict["data"][0]["quote"]["USD"]["price"]
        coin2_cmcRank = my_dict["data"][0]["cmc_rank"]
      elif current_coin == 3:
        coin3_price = my_dict["data"][0]["quote"]["USD"]["price"]
        coin3_cmcRank = my_dict["data"][0]["cmc_rank"]
      elif current_coin == 4:
        coin4_price = my_dict["data"][0]["quote"]["USD"]["price"]
        coin4_cmcRank = my_dict["data"][0]["cmc_rank"]
      elif current_coin == 5:
        coin5_price = my_dict["data"][0]["quote"]["USD"]["price"]
        coin5_cmcRank = my_dict["data"][0]["cmc_rank"]

for i in range (amount_of_coins):
  GenerateData()

print("\033[34m############## Specific data ##############\033[0m")
print("\033[34mCoin 1:\033[0m")
print("\033[34mCurrent price: \033[0m", coin1_price)
print("\033[34mCurrent cmc rank: \033[0m", coin1_cmcRank)
print("\033[34m---\033[0m")
print("\033[34mCoin 2:\033[0m")
print("\033[34mCurrent price: \033[0m", coin2_price)
print("\033[34mCurrent cmc rank: \033[0m", coin2_cmcRank)
print("\033[34m---\033[0m")
print("\033[34mCoin 3:\033[0m")
print("\033[34mCurrent price: \033[0m", coin3_price)
print("\033[34mCurrent cmc rank: \033[0m", coin3_cmcRank)
print("\033[34m---\033[0m")
print("\033[34mCoin 4:\033[0m")
print("\033[34mCurrent price: \033[0m", coin4_price)
print("\033[34mCurrent cmc rank: \033[0m", coin4_cmcRank)
print("\033[34m---\033[0m")
print("\033[34mCoin 5:\033[0m")
print("\033[34mCurrent price: \033[0m", coin5_price)
print("\033[34mCurrent cmc rank: \033[0m", coin5_cmcRank)
print("\033[34m###########################################\033[0m")