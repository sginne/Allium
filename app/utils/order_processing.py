from app import db,models,currency

def process_orders():
    orders = models.Orders.query.all()

