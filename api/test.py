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
    #print(ticker_url_pairs)
  print()
  print('MY PORTFOLIO')
  print()

  portfolio_value = 0.00
  last_updated = 0

  table = PrettyTable(['Asset', 'Amount Owned', convert + ' Value', 'Price', '1h', '24h', '7d'])

  with open("portfolio.txt") as inp:
      for line in inp:
          ticker, amount = line.split()
          ticker = ticker.upper()
          ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + str(ticker_url_pairs[ticker])


   response = session.get(ticker_url, params=parameters)
   results = json.loads(response.text)

   currency = results['data'][0]

   name = currency['name']
   symbols = currency['symbol']
   quotes = currency['quotes']['USD']
   hour_chng = quotes['percent_change_1h']
   day_chng = quotes['percent_change_24h']
   week_chng = quotes['percent_change_7d']
   price = quotes['price']

   value = float(price) * float(amount)

   portfolio += value

   value_string  = '{:.}'.format(round(value,2))

   table.add_row([name + ' (' + symbol + ')',
            '$' + value_string,
            '$' + str(price),
            str(hour_chng),
            str(day_chng),
            str(week_chng)])

    print(table)
    print()
    portfolio_value_string = '{:.}'.format(round(portfolio_value,2))

    last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

    print("Total Portfolio: " + portfolio_value_string)
    print()
    print("API result last updated on: " + last_updated_string)
