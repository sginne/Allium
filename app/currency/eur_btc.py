import json,urllib
from .. import utils
#a=utils.ZZ
class FiatCrypto:
    http=utils.http_module.work_horse()
    exchange_url='https://blockchain.info/ticker'
    exchange_rate=0
    def __init__(self):
        self.read_exchange_rate()
    def read_exchange_rate(self):
        data=self.http.json_loads(self.http.url_request(self.exchange_url))
        self.exchange_rate = data['EUR']['last']
        #with urllib.request.urlopen(self.exchange_url) as url:
        #    data = json.loads(url.read().decode())
        #    self.exchange_rate=data['EUR']['last']

