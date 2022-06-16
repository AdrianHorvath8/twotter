from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:pk>/", views.profile, name="profile"),
    path("account/<str:pk>/", views.account, name="account"),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),

    path('register/', views.register, name='register'),

]
