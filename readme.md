# CoinMarketCap API

**Info**

- The response will be put inside the response.json file. Every time you run the file the response.json will update the stats.

**Requirements:**

- Python 3
- CoinMarketCap API (https://pro.coinmarketcap.com/account/)
- `pip install requests`
- `pip3 install python-dotenv`

**How to start the project**

1. Rename the ".env.example" to ".env"
2. Add "apiKey = _(API key)_"
3. Run the file by typing "_python cmdAPI.py_" in the terminal or by running the "start.bat" file. There will be a 5 minute delay between runs because otherwise we will make more requests than allowed on the cmc API free tier! Please make sure to not exceed that amount so we can have a steady flow of data updates (There is a 45 request wiggle room per day!).

**Written by: Pontus Henriksson - https://github.com/pontushenriksson**
