from flask import Blueprint, jsonify
from models.product import Product

p_bp = Blueprint('products', __name__, url_prefix='/products')

###################################################
# Get for multiple base production volumes
###################################################
@p_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.serialize() for p in products])
