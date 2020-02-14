from app import db
#goods
class Goods(db.Model):
    """
    Class of goods to trade
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
