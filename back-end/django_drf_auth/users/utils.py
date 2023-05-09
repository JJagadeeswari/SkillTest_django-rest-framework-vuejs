from rest_framework_simplejwt.tokens import RefreshToken
import os


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def user_profile_pic_path(instance, filename):
    user_id = instance.id
    directory_path = 'userProfile/profilePic/{}/'.format(user_id)
    return os.path.join(directory_path, filename)
