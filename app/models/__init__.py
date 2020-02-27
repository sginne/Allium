#from app import db
#import app
from .. import db
from . import populate

all_tables=["items","pictures","picture_containers","fiat_currency","crypto_currency"]
class Fiat_currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name=db.Column(db.String(10))
    sign=db.Column(db.String(2))
    __tablename__ = "fiat_currency"

class Crypto_currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name=db.Column(db.String(10))
    sign=db.Column(db.String(2))
    __tablename__ = "crypto_currency"

#goods
class Item(db.Model):
    """
    Item model
    """
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(4096))

    price_fiat=db.Column(db.Numeric,nullable=False,default=0)
    price_fiat_id=db.Column(db.Integer,db.ForeignKey('fiat_currency.id'))
    price_fiat_relation=db.relationship("Fiat_currency")

    price_crypto=db.Column(db.Numeric,nullable=False,default=0)
    price_crypto_id=db.Column(db.Integer,db.ForeignKey('crypto_currency.id'))
    price_crypto_relation=db.relationship("Crypto_currency")

    fiat_crypto_main_flag=db.Column(db.String(1))

    __tablename__="items"

class Picture(db.Model):
    """Picture model."""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    picture =  db.Column(db.Text)
    __tablename__ = 'pictures'
