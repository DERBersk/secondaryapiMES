from flask import Blueprint, jsonify

from models.production_volume import ProductionVolume

pv_bp = Blueprint('productionvolume', __name__, url_prefix='/productionvolume')

###################################################
# Get for multiple base production volumes
###################################################
@pv_bp.route('/', methods=['GET'])
def get_production_volumes():
    production_volumes = ProductionVolume.query.all()
    return jsonify([pv.serialize() for pv in production_volumes])
