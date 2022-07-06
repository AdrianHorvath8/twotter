from unicodedata import name
from django.urls import path
from . import views
from django.db.models import Q

urlpatterns = [
    path('', views.posts, name='posts'),
    path("search/", views.search, name="search"),
    path("tag/<str:pk>/", views.tag_view, name="tag_view"),
    path("post_comments/<str:pk>/", views.post_comments, name="post_comments"),
    path("delete_post/<str:pk>/", views.delete_post, name="delete_post")
]

