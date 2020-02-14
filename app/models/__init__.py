from app import db
import app
all_tables=["goods"]
#goods
class Goods(db.Model):
    """
    Class of goods to trade
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    #picture = app.image_attachment('Image')
    __tablename__="goods"
