import os
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


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

except (ConnectionError, Timeout, TooManyRedirects) as e:
     print(e)

print()
print('MY PORTFOLIO')
print()

portfolio_value = 0.00

table = PrettyTable(['Asset', 'Amount Owned', ' Value', 'Price', '1h', '24h', '7d'])

with open("portfolio.txt") as inp:
    for line in inp:
        ticker, amount = line.split()
        ticker = ticker.upper()
        #print(ticker)
        tickery_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id='
        tickery_url += str(ticker_url_pairs[ticker])

        try:
          response = session.get(tickery_url, params=parameters)
          data = json.loads(response.text)
          #print(json.dumps(data, sort_keys=True, indent=4))

          objec = data['data'][str(ticker_url_pairs[ticker])]

          name = objec['name']
          last_updated = objec['last_updated']
          symbol = objec['symbol']
          quotes = objec['quote']['USD']
          hour_chng = quotes['percent_change_1h']
          day_chng = quotes['percent_change_24h']
          week_chng = quotes['percent_change_7d']
          price = quotes['price']

          value = float(price) * float(amount)

          if hour_chng > 0:
              hour_chng = Back.GREEN + str(hour_chng) + '%' + Style.RESET_ALL
          else:
              hour_chng = Back.RED + str(hour_chng) + '%' + Style.RESET_ALL

          if day_chng > 0:
              day_chng = Back.GREEN + str(day_chng) + '%' + Style.RESET_ALL
          else:
              day_chng = Back.RED + str(day_chng) + '%' + Style.RESET_ALL

          if week_chng > 0:
              week_chng = Back.GREEN + str(week_chng) + '%' + Style.RESET_ALL
          else:
              week_chng = Back.RED + str(week_chng) + '%' + Style.RESET_ALL

          portfolio_value += value

          value_string  = '{:,}'.format(round(value,2))

          table.add_row([name + ' (' + symbol + ')',
                        amount,
                        '$' + value_string,
                        '$' + str(price),
                        str(hour_chng),
                        str(day_chng),
                        str(week_chng)])

        except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)

print(table)
print()
portfolio_value_string = '{:,}'.format(round(portfolio_value,2))

print("Total Portfolio: " + Back.GREEN + "%" + portfolio_value_string + Style.RESET_ALL)
print()
print("API result last updated on: " + last_updated)
