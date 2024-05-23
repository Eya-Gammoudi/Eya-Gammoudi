from django.urls import path
from . import views

urlpatterns = [
    path('CS/', views.collectorSignup, name='collector_signup'),
    path('CL/', views.collectorLogin, name='collector_login'),
]