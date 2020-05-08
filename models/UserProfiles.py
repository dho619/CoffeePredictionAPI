import datetime
from Api import db, ma

class UserProfiles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    profile = db.relationship("Profile", back_populates="user_profiles")

    def __init__(self, user_id, profile_id):
        self.user_id = user_id
        self.profile_id = profile_id

#Definindo o Schema do Marshmallow para facilitar a utilização de JSON
class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'profile_id')

userProfile_schema = UserProfileSchema()
userProfiles_schema = UserProfileSchema( many = True )
