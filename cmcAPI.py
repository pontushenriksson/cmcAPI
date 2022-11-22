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
tokens = os.getenv('tokens')
tokens = tokens.split(' ')
tokens.sort()
author = os.getenv('author')
version = os.getenv('codeVersion')
githubRepo = os.getenv('githubRepo')
link = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol='
suffix = ""
number = 0
for i in range(len(tokens)):
  suffix += tokens[number]+','
  number += 1
url = link+suffix

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

# Make everything a function
def runTokens():
  number = 0;
  for i in range(len(tokens)):
    print(tokens[number])
    name = my_dict["data"][tokens[number]]["name"]
    symbol = my_dict["data"][tokens[number]]["symbol"]
    cmc_id = my_dict["data"][tokens[number]]["id"]
    price = my_dict["data"][tokens[number]]["quote"]["USD"]["price"]
    max_supply = my_dict["data"][tokens[number]]["max_supply"]
    circulating_supply = my_dict["data"][tokens[number]]["circulating_supply"]
    cmc_rank = my_dict["data"][tokens[number]]["cmc_rank"]
    market_dominance = my_dict["data"][tokens[number]]["quote"]["USD"]["market_cap_dominance"]
    number += 1

    # Prints the specific data we chose from the response. I have handpicked my idea of the 5 most important data points: name, symbol, price, rank, and market dominance, and use the earlier specified variables to print that data.
    print("\033[34mToken name: \033[0m", name)
    print("\033[34mToken symbol: \033[0m", symbol)
    print("\033[34mCMC id: \033[0m", cmc_id)
    print("\033[34mCurrent price: \033[0m", price,"$ USD per token")
    print("\033[34mMax supply (max number of tokens): \033[0m", max_supply)
    print("\033[34mCirculating supply (number of tokens that exist): \033[0m", circulating_supply)
    print("\033[34mCurrent cmc rank: \033[0m", cmc_rank)
    print("\033[34mCurrent market dominance: \033[0m", market_dominance,"%")
    if (number!=len(tokens)):
      print("\033[34m---\033[0m")

print("\033[34m############## Specific data ##############\033[0m")
runTokens()
print("\033[34m###########################################\033[0m")

print("\033[31m############## Information ##############\033[0m")
print("\033[31mAuthor: \033[0m" + author)
print("\033[31mCode version: \033[0m" + version)
print("\033[31mGithub Repo: \033[0m" + githubRepo)
print("\033[31m#########################################\033[0m")