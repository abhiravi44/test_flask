from app import db


class Well(db.Model):
    __tablename__ = 'wells'

    api_well__number = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    oil = db.Column(db.Float, nullable=False)
    gas = db.Column(db.Float, nullable=False)
    brine = db.Column(db.Float, nullable=False)

    def __init__(self, api_well_number, production_year, quarter, owner_name, county, township, well_name, well_number, oil, gas, brine, days):
        self.api_well_number = api_well_number
        self.oil = oil
        self.gas = gas
        self.brine = brine
