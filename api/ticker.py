from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id='
parameters = {

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2d155a56-c19a-4d72-bd91-c5b9e3812b20',
}

session = Session()
session.headers.update(headers)
id = 1
url += str(id) 

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(json.dumps(data, sort_keys=True, indent=4))

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
