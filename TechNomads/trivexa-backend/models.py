from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disease_name = db.Column(db.String(100), nullable=False)
    disease_url = db.Column(db.String(255))
    med_name = db.Column(db.String(100), nullable=False)
    med_url = db.Column(db.String(255))
    final_price = db.Column(db.String(100))
    price = db.Column(db.String(100))
    prescription_required = db.Column(db.String(100))
    drug_variant = db.Column(db.String(100))
    drug_manufacturer = db.Column(db.String(100))
    drug_manufacturer_origin = db.Column(db.String(100))
    drug_content = db.Column(db.String(255))
    generic_name = db.Column(db.String(100))
    img_urls = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Medicine {self.med_name}>'
