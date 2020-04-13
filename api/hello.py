from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

url = 'https://pro-api.coinmarketcap.com/v1/partners/flipside-crypto/fcas/listings/latest'
parameters = {

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d155a56-c19a-4d72-bd91-c5b9e3812b20',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  result = json.loads(response.text)
  #print(json.dumps(data, sort_keys=True, indent=4))
  data = result['data']
  ticker_url_pairs= {}
  for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url
    print(ticker_url_pairs[symbol])

except (ConnectionError, Timeout, TooManyRedirects) as e:
     print(e)
