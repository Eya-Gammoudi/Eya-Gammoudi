# backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import greener  # Ensure consistent naming

class greenerAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Rename the variable to avoid naming conflict
            greener_obj = greener.objects.get(Email=email)
            # Ensure that the password field is loaded
            greener_with_password = greener.objects.filter(pk=greener_obj.pk).values('password').first()
            if greener_with_password and check_password(password, greener_with_password['password']):
                return greener_obj
        except greener.DoesNotExist:
            return None
