from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post, Comment
from users.models import Profile, Chat, Message
from .serializers import PostsSerializer, ProfileSerializer
from rest_framework import status

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

        
        {"POST":"/api/bookmark"},
        {"GET":"/api/bookmark/id"},
        {"PUT":"/api/bookmark/id"},
        {"DELETE":"/api/bookmark/id"},
    ]
    return Response(routes)

@api_view(['GET','POST'])
def posts(request):
    posts = Post.objects.all()
    if request.method == "GET":
        serializer = PostsSerializer(posts, many = True)
        return Response(serializer.data)


    if request.method == "POST":
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET','PUT','DELETE'])
def post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        serializer = PostsSerializer(post, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def profiles(request):
    profiles = Profile.objects.all()
    if request.method == "GET":
        serializer = ProfileSerializer(profiles, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def profile(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == "GET":
        serializer = ProfileSerializer(profile, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)