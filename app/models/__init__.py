#from app import db
#import app
from .. import db
from . import populate
import enum

class Status(enum.Enum):
    placed = "placed"
    partially_paid = "partially_paid"
    fully_paid = "fully_paid"
    acknowledged = "acknowledged"
    processed = "processed"
    archived = "archived"
    

all_tables=["items","pictures","picture_containers","fiat_currency","crypto_currency","orders"]
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
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_wallet=db.Column(db.String(100))
    status=db.Column(db.Enum(Status),nullable=False,default=Status.placed)
    private_key=db.Column(db.Text)
    price_crypto=db.Column(db.Numeric,nullable=False,default=0)
    ordered_name = db.Column(db.String(64),nullable=False)
    contact_info = db.Column(db.String(64),nullable=False)
    address = db.Column(db.String(4096))
    comment = db.Column(db.String(4096))
    review = db.Column(db.String(4096))
    
    date=db.Column(db.Integer,nullable=False)
    
    total_received=db.Column(db.Numeric,nullable=False,default=0)
    final_balance=db.Column(db.Numeric,nullable=False,default=0)
    n_tx=db.Column(db.Numeric,nullable=False,default=0)

	
    __tablename__ = "orders"


#goods
class Item(db.Model):
    """
    Item model
    """
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(4096))
    short_description=db.Column(db.String(256))
    amount_palette=db.Column(db.String(256),default="1 2 3 4 5", nullable=False)
    pic_name=db.Column(db.String(64))
    amount=db.Column(db.Integer,default=0, nullable=False)

    price_fiat=db.Column(db.Numeric,nullable=False,default=0)
    price_fiat_id=db.Column(db.Integer,db.ForeignKey('fiat_currency.id'))
    price_fiat_relation=db.relationship("Fiat_currency")

    price_crypto=db.Column(db.Numeric,nullable=False,default=0)
    price_crypto_id=db.Column(db.Integer,db.ForeignKey('crypto_currency.id'))
    price_crypto_relation=db.relationship("Crypto_currency")

    fiat_crypto_main_flag=db.Column(db.String(1),default="fiat")

    __tablename__="items"

class Picture(db.Model):
    """Picture model."""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    picture =  db.Column(db.Text)
    __tablename__ = 'pictures'
