from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='user_list'),
    path('get-users', views.get_alluser, name='get_alluser'),
    path('groups', views.groups, name='group_list'),
]
