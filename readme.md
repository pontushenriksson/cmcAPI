# CoinMarketCap API

**Info**

- The API response will be saved as a JSON file which is called "response.json". Every time you run the project the "response.json" file will update the data to the new data received from the new API request. We use environment variables as a secure way to store our config files. _*Never*_ remove the .gitIgnore file, it is used to prevent the leak of the environment variables!

**Requirements:**

- Python 3
- CoinMarketCap API (https://pro.coinmarketcap.com/account/)
- `pip install requests`
- `pip3 install python-dotenv`
- `phpMyAdmin`
- `MySQL`

**How to start the project**

1. Duplicate the ".env.example" file and rename the new file to ".env".
2. Add `apiKey = (API key)` to the new .env file and change "_(API key)_" to the CoinMarketCap API key.
3. Run the file by typing `python cmdAPI.py` in the terminal or by running the "start.bat" file. There will be a 5-minute delay between runs because otherwise, we will make more requests than allowed on the CoinMarketCap API free tier! Please make sure to not exceed that amount so we can have a steady flow of data updates (There is a 45-request wiggle room per day!).

**Copyright and disclaimer**
Copyright (C) Pontus Henriksson - All Rights Reserved.

THE CONTENTS OF THIS PROJECT ARE PROPRIETARY AND CONFIDENTIAL.
UNAUTHORIZED COPYING, TRANSFERRING OR REPRODUCTION OF THE CONTENTS OF THIS PROJECT, VIA ANY MEDIUM IS STRICTLY PROHIBITED.

The receipt or possession of the source code and/or any parts thereof does not convey or imply any right to use them
for any purpose other than the purpose for which they were provided to you.

The software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to
the warranties of merchantability, fitness for a particular purpose and non infringement.
In no event shall the authors or copyright holders be liable for any claim, damages or other liability,
whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software
or the use or other dealings in the software.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**Written by: Pontus Henriksson - https://github.com/pontushenriksson**
