from app import db


class Well(db.Model):
    __tablename__ = 'wells'

    id = db.Column(db.Integer, primary_key=True)
    api_well_number = db.Column(db.String(50), unique=True, nullable=False)
    production_year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.Float, nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    township = db.Column(db.String(50), nullable=False)
    well_name = db.Column(db.String(100), nullable=False)
    well_number = db.Column(db.String(50), nullable=False)
    oil = db.Column(db.Float, nullable=False)
    gas = db.Column(db.Float, nullable=False)
    brine = db.Column(db.Float, nullable=False)
    days = db.Column(db.Integer, nullable=False)

    def __init__(self, api_well_number, production_year, quarter, owner_name, county, township, well_name, well_number, oil, gas, brine, days):
        self.api_well_number = api_well_number
        self.production_year = production_year
        self.quarter = quarter
        self.owner_name = owner_name
        self.county = county
        self.township = township
        self.well_name = well_name
        self.well_number = well_number
        self.oil = oil
        self.gas = gas
        self.brine = brine
        self.days = days
