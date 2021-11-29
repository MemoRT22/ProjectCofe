from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class UserBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None):
        print('*'*50)
        print("Authentication is done")
        print(username, password)
        print('*'*50)
        user = None
        if True:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                print("Not an existing user")
            return user
        def get_user(self,user_id):
            try:
                return User.objects.get(pk= user_id)
            except User.DoesNotExist:
                return None
        
        