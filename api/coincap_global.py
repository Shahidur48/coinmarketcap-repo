 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
  'convert':'BDT'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d155a56-c19a-4d72-bd91-c5b9e3812b20',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

active_currencies = data['data']['active_cryptocurrencies']
active_exchange = data['data']['active_exchanges']
active_market_pairs = data['data']['active_market_pairs']
btc_dom = data['data']['btc_dominance']
alt_market_cap = data['data']['quote']['USD']['altcoin_market_cap']
#print('There are currently ' + str(active_currencies)+ ' active currencies ' + ' and ' + str(active_exchange) + ' active exchane' + ' where total ' + str(active_market_pairs)+' active market')
#print('Total dominance '+ str(btc_dom) + ' and ' + str(alt_market_cap)+ ' altcoin market cap')
