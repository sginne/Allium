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
        self.update()
    def update(self):
        self.read_exchange_rate()
    def link(self,address,amount,message,body):
        return ("<a rel='payment' href='bitcoin:{}?amount={}?message={}'>{}</a>".format(address,amount,message,body))
    def read_exchange_rate(self):
        data=self.http.json_loads(self.http.url_request(self.exchange_url))
        self.exchange_rate = data['EUR']['last']
    def read_wallet(self, wallet):
        data=self.http.json_loads(self.http.url_request("https://blockchain.info/rawaddr/{}".format(wallet)))
        return data
    def read_wallet_final_balance(self,wallet):
        return self.read_wallet(wallet)['final_balance']
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
        
    def private_to_wif(self,priv, verbose=False):
        ''' Produce a WIF from private key'''
        _priv = priv.lower() 
        if verbose : print("Private key: "+_priv)
		# Add a 0x80 byte in front of it
        priv_add_x80 = "80" + _priv
        if verbose : print("Private with x80 at beginning: "+priv_add_x80)
        # Perform SHA-256 hash on the extended key 
        first_sha256 = self.sha256(priv_add_x80)
        if verbose : print("sha256: " + first_sha256.upper())
        # Perform SHA-256 hash on result of SHA-256 hash 
        second_sha256 = self.sha256(first_sha256)
        if verbose : print("sha256: " + second_sha256.upper())
        # Take the first 4 bytes of the second SHA-256 hash, this is the checksum 
        first_4_bytes = second_sha256[0:8]
        if verbose : print("First 4 bytes: " + first_4_bytes)
        # Add the 4 checksum bytes from point 5 at the end of the extended key from point 2 
        resulting_hex = priv_add_x80 + first_4_bytes
        if verbose : print("Resulting WIF in HEX: " + resulting_hex)
        # Convert the result from a byte string into a base58 string using Base58Check encoding. This is the Wallet Import Format 
        result_wif = base58.b58encode(resulting_hex)
        if verbose : print("Resulting WIF: " + result_wif)
        return result_wif
        
    def sha256(self,arg) :
	    ''' Return a sha256 hash of a hex string '''
	    byte_array = bytearray.fromhex(arg)
	    m = hashlib.sha256()
	    m.update(byte_array)
	    return m.hexdigest()

