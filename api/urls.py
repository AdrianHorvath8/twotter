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
    path("comments/", views.comments),
    path("comments/<str:pk>/", views.comment),
    path("chats/", views.chats),
    path("chats/<str:pk>/", views.chat),
    path("messages/", views.messages),
    path("messages/<str:pk>/", views.message),
    path("bookmarks/", views.bookmarks),
    path("bookmarks/<str:pk>/", views.bookmark),
    path("topics/", views.topics),
    path("topics/<str:pk>/", views.topic),



    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]