
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
   
    path('register',v.register),
    path('login',v.login_view),
    path('logout',v.logout_view),
    path('user_posts',v.user_posts),
    path('d_post',v.delete_post),
    path('index',v.index),
    path('profile',v.my_profile),
    path('e_post',v.edit_profile),
    path('e_usr',v.edit_reg),
    path('sort',v.sort_by_name),
    path('d_cmnt',v.delete_cmnt),
    path('comment',v.comments),
    
    
    
    
]
