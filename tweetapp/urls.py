from django.urls import path 
from .views import *

urlpatterns = [
    path('',tweet_list,name='tweet_list'),
    path('register/',register,name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-tweet/',tweet_create,name='tweet_create'),
    path('tweet-update/<int:tweet_id>/',tweet_edit,name='tweet_edit'),
    path('tweet-delete/<int:tweet_id>/',tweet_delete,name='tweet_delete'),
]