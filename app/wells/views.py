from flask import jsonify, request
from app import app
from app.models import Well
from app.schema.wells import WellSchema
from app.utils import paginated_response

wells_schema = WellSchema(many=True)

@app.route('/data', methods=['GET'])
def get_products():
    try:
        well = request.args.get('well')
        county = request.args.get('county')
        well_number = request.args.get('well_number')
        limit = request.args.get('limit', 10, type=int)
        offset = request.args.get('offset', 0, type=int)
        query = Well.query
        if well:        
            all_wells = query.filter_by(api_well__number=well)
        if county:
            all_wells = query.filter_by(county=county)
        if well_number:
            all_wells = query.filter_by(well_number=well_number)
        paginated_wells = all_wells.limit(limit).offset(offset)
        result = wells_schema.dump(paginated_wells.all())
        return jsonify(paginated_response(result, paginated_wells))
    except Exception as ex:
        return jsonify({"Error":str(ex)})