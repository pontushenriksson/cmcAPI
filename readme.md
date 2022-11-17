# CoinMarketCap API

**Info**

- The API response will be saved as a JSON file which is called "response.json". Every time you run the project the "response.json" file will update the data to the new data received from the new API request. We use environment variables as a secure way to store our config files. _*Never*_ remove the .gitIgnore file, it is used to prevent the leak of the environment variables!

**Requirements:**

- Python 3
- CoinMarketCap API (https://pro.coinmarketcap.com/account/)
- `pip install requests`
- `pip3 install python-dotenv`

**How to start the project**

1. Duplicate the ".env.example" file and rename the new file to ".env".
2. Add `apiKey = (API key)` to the new .env file and change "_(API key)_" to the CoinMarketCap API key.
3. Run the file by typing `python cmdAPI.py` in the terminal or by running the "start.bat" file. There will be a 5-minute delay between runs because otherwise, we will make more requests than allowed on the CoinMarketCap API free tier! Please make sure to not exceed that amount so we can have a steady flow of data updates (There is a 45-request wiggle room per day!).

**If there are any bugs with the current build please add those bugs in the `bugs.md` file so they can be fixed as soon as possible!**

**Written by: Pontus Henriksson - https://github.com/pontushenriksson**
