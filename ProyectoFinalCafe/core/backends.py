from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class UserBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None):
        user = None
        if username is None or password is None:
            return
        try:
            user = User._default_manager.get_by_natural_key(username)
        except User.DoesNotExist:
                print("No existe el usuario")
        if user is not None and user.check_password(password):
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                print("Password incorrecto")
            return user
            
    def get_user(self,user_id):
        try:
            return User.objects.get(pk= user_id)
        except User.DoesNotExist:
            return None