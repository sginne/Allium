import json,urllib
from .. import utils
import ecdsa,hashlib,binascii,base58


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
        return ecdsaPrivateKey.to_string()
    
    def address_from_key(self, private):
        ecdsaPrivateKey=ecdsa.SigningKey.from_string(private,curve=ecdsa.SECP256k1)
        ecdsaPublicKey = '04' +  ecdsaPrivateKey.get_verifying_key().to_string().hex()
        #print("ECDSA Public Key: ", ecdsaPublicKey)
        hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
        ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
        prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
        hash = prependNetworkByte
        for x in range(1,3):
            hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
            #print( x, " : ", hash)
        cheksum = hash[:8]
        appendChecksum = prependNetworkByte + cheksum
        bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
        #print("Bitcoin Address: ", bitcoinAddress.decode('utf8'))
        return bitcoinAddress.decode("utf-8")

