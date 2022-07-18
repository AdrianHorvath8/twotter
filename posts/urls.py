from unicodedata import name
from django.urls import path
from . import views
from django.db.models import Q

urlpatterns = [
    path('', views.posts, name='posts'),
    path("search/", views.search, name="search"),
    path("post_comments/<str:pk>/", views.post_comments, name="post_comments"),
    path("topic/<str:pk>/", views.topic, name="topic"),
    path("delete_post/<str:pk>/", views.delete_post, name="delete_post"),
    path("delete_comment/<str:pk>/", views.delete_comment, name="delete_comment"),
    path("post_like/<str:pk>/", views.post_like, name="post_like"),
    path("post_remove_like/<str:pk>/", views.post_remove_like, name="post_remove_like"),
    path("comment_like/<str:pk>/", views.comment_like, name="comment_like"),
    path("comment_remove_like/<str:pk>/", views.comment_remove_like, name="comment_remove_like"),
    path("bookmark/", views.bookmark, name="bookmark"),
    path("add_post_to_bookmark/<str:pk>/", views.add_post_to_bookmark, name="add_post_to_bookmark"),
    path("remove_post_from_bookmark/<str:pk>/", views.remove_post_from_bookmark, name="remove_post_from_bookmark"),

]

