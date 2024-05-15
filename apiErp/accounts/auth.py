from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User


class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s)')
        user_exists = User.objects.filter(email=email).exists()
        
        if not user_exists:
            raise exception_auth
        user = User.objects.filter(email=email).first()
        
        if not check_password(password, user.password):
            raise exception_auth
        
        return user