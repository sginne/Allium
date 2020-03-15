import json,urllib
class FiatCrypto:

    exchange_url='https://blockchain.info/ticker'
    exchange_rate=0
    def __init__(self):
        self.read_exchange_rate()
    def read_exchange_rate(self):
        with urllib.request.urlopen(self.exchange_url) as url:
            data = json.loads(url.read().decode())
            self.exchange_rate=data['EUR']['last']

