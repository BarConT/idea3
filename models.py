from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, password):
        self.id = id
        self.name = name 
        self.password = password   
        # self.password = generate_password_hash(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

users = []
user = User(1 , 'admin', 'pbkdf2:sha256:150000$5oClIM0i$c155be080802a2299bf20f891ea9e542c8fb11ea4a5927d390c36d2d91252a60')
users.append(user)

def get_user(name):
    for user in users:
        if user.name == name:
            return user
    return None