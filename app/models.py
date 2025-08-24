from app import db


class Well(db.Model):
    __tablename__ = 'wells'

    api_well__number = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    oil = db.Column(db.Float, nullable=False)
    gas = db.Column(db.Float, nullable=False)
    brine = db.Column(db.Float, nullable=False)
    county = db.Column(db.String(50), nullable=True) 
    well_number = db.Column(db.String(50),nullable=True)
    production_year = db.Column(db.Integer(), nullable=True)

    def __init__(self, api_well_number, county, well_number, oil, gas, brine):
        self.api_well_number = api_well_number
        self.oil = oil
        self.gas = gas
        self.brine = brine
        self.county = county
        self.well_number = well_number
