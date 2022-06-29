from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='user_list'),
]
