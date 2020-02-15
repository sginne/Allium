from app import db
import app
all_tables=["goods","good_picture"]
#goods
class Goods(db.Model):
    """
    Class of goods to trade
    """
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    names = db.Column(db.String(64))
    description = db.Column(db.String(4096))
    picture = app.image_attachment('Image')
    __tablename__="goods"
class GoodsPicture(db.Model, app.Image):
    """Goods picture model."""
    good_id = db.Column(db.Integer, db.ForeignKey('goods.id'), primary_key=True)
    good_picture = app.relationship('Goods')
    __tablename__ = 'good_picture'
