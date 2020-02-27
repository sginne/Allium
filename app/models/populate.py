from .. import models
def populate_tables(db):
    fiat=[]
    fiat.append(models.Fiat_currency(name="Euro",sign="€"))

    crypto=[]
    crypto.append(models.Crypto_currency(name="bitcoin",sign="btc"))

    for fiat_i in fiat:
        if not models.Fiat_currency.query.filter_by(name=fiat_i.name).first():
            db.session.add(fiat_i)
            db.session.commit()
    for crypto_i in crypto:
        if not models.Crypto_currency.query.filter_by(name=crypto_i.name).first():
            db.session.add(crypto_i)
            db.session.commit()