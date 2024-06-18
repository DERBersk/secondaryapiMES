# import external sources
from flask import Flask
import json
from flask_cors import CORS
# import functions and data
from extensions import db

def create_app():
    app = Flask(__name__.split(".")[0])
    CORS(app)
    
    with open('config.json', 'r') as file:
        config = json.load(file)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config["DATABASE"]
    # Import routes
    from routes.production_volume_routes import pv_bp
    from routes.product_routes import p_bp
    # Register blueprints
    app.register_blueprint(pv_bp)
    app.register_blueprint(p_bp)
    return app

app = create_app()
db.init_app(app)
with app.app_context():
    db.create_all()
# app.run(debug=True, host='0.0.0.0')
if __name__ == "__main__":
    app.run(debug=True)