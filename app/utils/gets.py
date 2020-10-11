from ..models.Users import Users
from ..models.Profiles import Profiles

def get_user_by_email_or_id(args):
    if not('id' in args or 'email' in args):
        return None

    result = []

    if 'id' in args:
        try:
            id = args['id']
        except:
            return None
        result = Users.query.get(id)
    elif 'email' in args:
        user = Users.query.filter_by(email=args['email']).first()

    return result

def get_profile_by_user(user):
    if not user:
        return None

    profile = Profiles.query.filter_by(id=user.profile_id).first()
    return profile.name.lower
