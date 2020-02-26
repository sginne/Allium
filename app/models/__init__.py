#from app import db
#import app
from .. import db
from . import populate

all_tables=["items","pictures","picture_containers","fiat_currency"]
class Fiat_currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(10))
    sign=db.Column(db.String(2))
    __tablename__ = "fiat_currency"


#goods
class Item(db.Model):
    """
    Item model
    """
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    price_fiat = db.Column(db.Numeric)
    description = db.Column(db.String(4096))

    __tablename__="items"
class Picture(db.Model):
    """Picture model."""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    picture =  db.Column(db.Text)
    __tablename__ = 'pictures'
