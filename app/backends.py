from django.contrib.auth.backends import ModelBackend
from .models import User

class MSSVBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(mssv=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
