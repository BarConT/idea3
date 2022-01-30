from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from run import db

class User(db.Model, UserMixin):

    __tablename__ = 'idea3_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) 
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
            return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()

class Comida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Comida {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_categoria(categoria_id):
        return Comida.query.filter_by(categoria=categoria_id).first() #quitar el first() o query.all()
    
    @staticmethod
    def get_by_id(id):
        return Comida.query.filter_by(id=id).first()

    @staticmethod
    def get_all():
        return Comida.query.all()

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(256), nullable=False)

    @staticmethod
    def get_all():
        return Categoria.query.all()
