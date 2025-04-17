import json
import requests
import sys
respond = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(json.dumps(respond.json(),indent=2))
usd_rate = float(respond.json()['bpi']['USD']['rate'].replace(',',''))
num = 0
try:
    if len(sys.argv) == 1:
        print('Missing command-line argument ')
    elif len(sys.argv) > 2:
        print('Command-line argument is not a number')
    else:
        num = float(sys.argv[1])
        print('$' + str(num * usd_rate))
except ValueError:
    print('Command-line argument is not a number')

