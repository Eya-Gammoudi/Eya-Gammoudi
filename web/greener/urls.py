from django.urls import path
from . import views

urlpatterns = [
    path('GS/', views.greenerSignup, name='greener_signup'),
    path('GL/', views.greenerLogin, name='greener_login'),
    path('home/', views.greenerhome, name='greener_home'),
]