from extensions import db
import datetime

class ProductionVolume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'date':self.date,
            'amount': self.amount
        }