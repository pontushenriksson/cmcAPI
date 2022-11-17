# Import all the necessary things.
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
load_dotenv()

# The API key entered in the ".env" file will get loaded and be saved as the "apiKey" variable.
apiKey = os.getenv('apiKey')
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=XMR,ETH,DOGE,BTC,RVN'

# Enter the parameters and routing information that the API needs to receive a data request.
parameters = {
}
headers = {
    # Specifies what response type we accept and parses the apiKey.
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKey,
}
# Generates a session to be used to retrieve information. Each session is the same thing as one request.
session = Session()
session.headers.update(headers)
try:
  # Processing the response, loading the response as a JSON file, converting it to text and then printing the result.
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print("\033[32m############## All data ##############\033[0m")
  print(data)
  print("\033[32m#######################################\033[0m")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
    
# Creating the "response.json" file and writing the API response data to that file. To achieve this we just call the dump() function from the JSON library.
with open('response.json', 'w') as json_file:
  json.dump(data, json_file)
with open("response.json", "r") as f:
  my_dict = json.load(f)

# Creating easier-to-read variable names so you don't need to use the relative JSON data path.
BTC_name = my_dict["data"]["BTC"]["name"]
BTC_symbol = my_dict["data"]["BTC"]["symbol"]
BTC_price = my_dict["data"]["BTC"]["quote"]["USD"]["price"]
BTC_cmcRank = my_dict["data"]["BTC"]["cmc_rank"]
BTC_market_dominance = my_dict["data"]["BTC"]["quote"]["USD"]["market_cap_dominance"]

DOGE_name = my_dict["data"]["DOGE"]["name"]
DOGE_symbol = my_dict["data"]["DOGE"]["symbol"]
DOGE_price = my_dict["data"]["DOGE"]["quote"]["USD"]["price"]
DOGE_cmcRank = my_dict["data"]["DOGE"]["cmc_rank"]
DOGE_market_dominance = my_dict["data"]["DOGE"]["quote"]["USD"]["market_cap_dominance"]

ETH_name = my_dict["data"]["ETH"]["name"]
ETH_symbol = my_dict["data"]["ETH"]["symbol"]
ETH_price = my_dict["data"]["ETH"]["quote"]["USD"]["price"]
ETH_cmcRank = my_dict["data"]["ETH"]["cmc_rank"]
ETH_market_dominance = my_dict["data"]["ETH"]["quote"]["USD"]["market_cap_dominance"]

RVN_name = my_dict["data"]["RVN"]["name"]
RVN_symbol = my_dict["data"]["RVN"]["symbol"]
RVN_price = my_dict["data"]["RVN"]["quote"]["USD"]["price"]
RVN_cmcRank = my_dict["data"]["RVN"]["cmc_rank"]
RVN_market_dominance = my_dict["data"]["RVN"]["quote"]["USD"]["market_cap_dominance"]

XMR_name = my_dict["data"]["XMR"]["name"]
XMR_symbol = my_dict["data"]["XMR"]["symbol"]
XMR_price = my_dict["data"]["XMR"]["quote"]["USD"]["price"]
XMR_cmcRank = my_dict["data"]["XMR"]["cmc_rank"]
XMR_market_dominance = my_dict["data"]["XMR"]["quote"]["USD"]["market_cap_dominance"]

# Prints the specific data we chose from the response. I have handpicked my idea of the 5 most important data points: name, symbol, price, rank, and market dominance, and use the earlier specified variables to print that data.
print("\033[34m############## Specific data ##############\033[0m")
print("\033[34mToken name: \033[0m", BTC_name)
print("\033[34mToken symbol: \033[0m", BTC_symbol)
print("\033[34mCurrent price: \033[0m", BTC_price,"$ USD per token")
print("\033[34mCurrent cmc rank: \033[0m", BTC_cmcRank)
print("\033[34mCurrent market dominance: \033[0m", BTC_market_dominance,"%")

print("\033[34m---\033[0m")

print("\033[34mToken name: \033[0m", DOGE_name)
print("\033[34mToken symbol: \033[0m", DOGE_symbol)
print("\033[34mCurrent price: \033[0m", DOGE_price,"$ USD per token")
print("\033[34mCurrent cmc rank: \033[0m", DOGE_cmcRank)
print("\033[34mCurrent market dominance: \033[0m", DOGE_market_dominance,"%")

print("\033[34m---\033[0m")

print("\033[34mToken name: \033[0m", ETH_name)
print("\033[34mToken symbol: \033[0m", ETH_symbol)
print("\033[34mCurrent price: \033[0m", ETH_price,"$ USD per token")
print("\033[34mCurrent cmc rank: \033[0m", ETH_cmcRank)
print("\033[34mCurrent market dominance: \033[0m", ETH_market_dominance,"%")

print("\033[34m---\033[0m")

print("\033[34mToken name: \033[0m", RVN_name)
print("\033[34mToken symbol: \033[0m", RVN_symbol)
print("\033[34mCurrent price: \033[0m", RVN_price,"$ USD per token")
print("\033[34mCurrent cmc rank: \033[0m", RVN_cmcRank)
print("\033[34mCurrent market dominance: \033[0m", RVN_market_dominance,"%")

print("\033[34m---\033[0m")

print("\033[34mToken name: \033[0m", XMR_name)
print("\033[34mToken symbol: \033[0m", XMR_symbol)
print("\033[34mCurrent price: \033[0m", XMR_price,"$ USD per token")
print("\033[34mCurrent cmc rank: \033[0m", XMR_cmcRank)
print("\033[34mCurrent market dominance: \033[0m", XMR_market_dominance,"%")
print("\033[34m###########################################\033[0m")