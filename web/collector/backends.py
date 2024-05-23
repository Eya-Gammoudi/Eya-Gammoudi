# backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import collector  # Ensure consistent naming

class collectorAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Rename the variable to avoid naming conflict
            collector_obj = collector.objects.get(Email=email)
            # Ensure that the password field is loaded
            collector_with_password = collector.objects.filter(pk=collector_obj.pk).values('password').first()
            if collector_with_password and check_password(password, collector_with_password['password']):
                return collector_obj
        except collector.DoesNotExist:
            return None
