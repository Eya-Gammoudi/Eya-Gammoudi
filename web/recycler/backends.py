# backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import recycler  # Ensure consistent naming

class recyclerAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Rename the variable to avoid naming conflict
            recycler_obj = recycler.objects.get(Email=email)
            # Ensure that the password field is loaded
            recycler_with_password = recycler.objects.filter(pk=recycler_obj.pk).values('password').first()
            if recycler_with_password and check_password(password, recycler_with_password['password']):
                return recycler_obj
        except recycler.DoesNotExist:
            return None
