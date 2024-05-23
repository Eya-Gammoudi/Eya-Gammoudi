from django.urls import path
from . import views

urlpatterns = [
    path('RS/', views.recyclerSignup, name='recycler_signup'),
    path('RL/', views.recyclerLogin, name='recycler_login'),
    path('home/', views.recyclerhome, name='recycler_home'),
]