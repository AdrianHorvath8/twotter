from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", views.get_routes),
    path("posts/", views.posts),
    path("posts/<str:pk>/", views.post),
    path("profiles/", views.profiles),
    path("profiles/<str:pk>/", views.profile),


    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]