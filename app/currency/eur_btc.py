import json,urllib
class EurBtc:

    exchange_url='https://blockchain.info/ticker'
    def __init__(self):

    def read_exchange_rate(self):
        with urllib.request.urlopen(self.exchange_url) as url:
            data = json.loads(url.read().decode())
            print(data)

