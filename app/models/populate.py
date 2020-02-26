from .. import models
def populate_tables(db):
    euro=models.Fiat_currency(name="Euro",sign="€")
    if not models.Fiat_currency.query.filter_by(name="Euro").first():
        euro = models.Fiat_currency(name="Euro", sign="€")
        db.session.add(euro)
        db.session.commit()