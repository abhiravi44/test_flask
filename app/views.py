from flask import jsonify, request
from app import app
from app.models import Well
from app.schema import WellSchema

well_schema = WellSchema()
wells_schema = WellSchema(many=True)

@app.route('/data', methods=['GET'])
def get_products():
    well = request.args.get('well')
    print(well)         
    all_wells = Well.query.filter_by(api_well__number=well).all()  
    print("all wells", all_wells)
    result = wells_schema.dump(all_wells)
    return jsonify(result)