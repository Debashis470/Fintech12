# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('secure-data/', views.secure_data, name='secure_data'),
]
