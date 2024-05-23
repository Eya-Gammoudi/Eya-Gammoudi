from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.gis.db.models import PointField
from django.contrib.gis.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class collector(AbstractBaseUser):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)  # Change 'Email' to 'email'
    password = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Location = gis_models.PointField(srid=4326, default='POINT(0 0)')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)  # Nouveau champ pour l'approbation



    USERNAME_FIELD = 'Email'  # Set the USERNAME_FIELD to 'email'
    REQUIRED_FIELDS = ['FirstName', 'LastName', 'PhoneNumber']  # Add any other required fields

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    def get_full_name(self):
        return f"{self.FirstName} {self.LastName}"

    def get_short_name(self):
        return self.FirstName