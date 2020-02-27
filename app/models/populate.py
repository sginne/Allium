from .. import models
def populate_tables(db):
    fiat=[]
    fiat.append(models.Fiat_currency(name="Euro",sign="€"))

    if not models.Fiat_currency.query.filter_by(name=fiat[0].name).first():
        #euro = models.Fiat_currency(fiat[0])
        db.session.add(fiat[0])
        db.session.commit()