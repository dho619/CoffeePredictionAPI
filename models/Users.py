import datetime
from Api import db, ma

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name', 'created_at', 'updated_at')

user_schema = UsersSchema()
users_schema = UsersSchema( many = True )
