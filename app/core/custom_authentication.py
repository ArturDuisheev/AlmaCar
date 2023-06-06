from django.contrib.auth.backends import BaseBackend
from account.models import User


class AuthenticationWithoutPassword(BaseBackend):

    def authenticate(self, request, phone_number=None):
        if phone_number is None:
            phone_number = request.data.get('username', '')
        try:
            return User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None