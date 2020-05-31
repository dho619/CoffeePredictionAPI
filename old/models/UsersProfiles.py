from Api import db

usersProfiles = db.Table('usersProfiles', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('profile_id', db.Integer, db.ForeignKey('profiles.id'))
)
