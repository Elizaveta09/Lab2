import requests
import json
import time

def fun():
    return requests.get('https://blockchain.info/ru/ticker').text

a = input()
b = {}
d = json.loads(fun())
b = d[a]
print(b['buy'])

"""while True:
    d = json.loads(fun())
    print(d['RUB'])
    time.sleep(5)"""