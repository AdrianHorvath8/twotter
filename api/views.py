from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post, Comment
from users.models import Profile, Chat, Message
from .serializers import PostsSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {"GET":"/api/posts"},
        {"POST":"/api/posts"},
        {"GET":"/api/posts/id"},
        {"PUT":"/api/posts/id"},
        {"DELETE":"/api/posts/id"},

        {"GET":"/api/profiles"},
        {"POST":"/api/profiles"},
        {"GET":"/api/profiles/id"},
        {"PUT":"/api/profiles/id"},
        {"DELETE":"/api/profiles/id"},

        {"GET":"/api/comments"},
        {"POST":"/api/comments"},
        {"GET":"/api/comments/id"},
        {"PUT":"/api/comments/id"},
        {"DELETE":"/api/comments/id"},

        {"GET":"/api/chats"},
        {"POST":"/api/chats"},
        {"GET":"/api/chats/id"},
        {"PUT":"/api/chats/id"},
        {"DELETE":"/api/chats/id"},
    ]
    return Response(routes)

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostsSerializer(posts, many = True)
    return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
def post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        serializer = PostsSerializer(post, many = False)
    

    return Response(serializer.data)