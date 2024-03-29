from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:pk>/", views.profile, name="profile"),
    path("account/<str:pk>/", views.account, name="account"),
    path("user_chats/<str:pk>/", views.user_chats, name="user_chats"),
    path("user_chat/<str:pk>/", views.user_chat, name="user_chat"),
    path("create_chat/<str:pk>/", views.create_chat, name="create_chat"),
    path("following/<str:pk>/", views.following, name="following"),
    path("unfollowing/<str:pk>/", views.unfollowing, name="unfollowing"),
    path("followers_users/<str:pk>/", views.followers_users, name="followers_users"),
    path("following_users/<str:pk>/", views.following_users, name="following_users"),

    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),

]
