import json,urllib
from .. import utils
import ecdsa


#a=utils.ZZ
class FiatCrypto:
    http=utils.http_module.work_horse()
    exchange_url='https://blockchain.info/ticker'
    exchange_rate=0
    fiat_name="€"
    crypto_name="₿"
    def __init__(self):
        self.read_exchange_rate()
    def read_exchange_rate(self):
        data=self.http.json_loads(self.http.url_request(self.exchange_url))
        self.exchange_rate = data['EUR']['last']
    def generate_private_key(self):
        ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)	
        return ecdsaPrivateKey

