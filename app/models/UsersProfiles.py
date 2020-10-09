from app import db

usersProfiles = db.Table('usersProfiles', db.Model.metadata,
    db.Column('user_id', db.String(37), db.ForeignKey('users.id')),
    db.Column('profile_id', db.String(37), db.ForeignKey('profiles.id'))
)
