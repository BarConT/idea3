from app import db

class Comida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String)
    
    def __repr__(self):
        return f'<Comida {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Comida.query.get(id)

    @staticmethod
    def get_all():
        return Comida.query.all()

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(256), nullable=False)

    @staticmethod
    def get_all():
        return Categoria.query.all()
