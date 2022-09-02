from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='user_list'),
    path('get-users', views.get_alluser, name='get_alluser'),
    path('postgroup', views.creategroup, name='creatgroup'),
    path('groups', views.groups, name='group_list'),
    path('login', views.login_view, name='login'),
    path('post-login', views.user_login, name='post_login'),
   
]
