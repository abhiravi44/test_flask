from app import ma
from app.models import Well

class WellSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        load_instance = True
