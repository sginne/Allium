from app import db
import app

all_tables=["items","pictures","picture_containers"]
#goods
class Item(db.Model):
    """
    Item model
    """
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(4096))

    __tablename__="items"
class Picture(db.Model):
    """Picture model."""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    picture =  db.Column(db.Text)
    __tablename__ = 'pictures'
#class PictureContainer(db.Model,app.Image):
#    """Picture container model."""
#    picture_id=db.Column(db.Integer,db.ForeignKey('pictures.id'),primary_key=True)
#    picture=db.relationship("Picture")
#    __tablename__ ='picture_containers'