from extensions import db

class Product(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    description2 = db.Column(db.String(100))
    
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'description2': self.description2
        }