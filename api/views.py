from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment, Bookmark, Topic
from users.models import Profile, Chat, Message
from .serializers import PostsSerializer, ProfileSerializer, UserSerializer, CommentSerializer, ChatSerializer, MessageSerializer, BookmarkSerializer, TopicSerializer
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

        {"GET":"/api/messages"},
        {"POST":"/api/messages"},
        {"GET":"/api/messages/id"},
        {"PUT":"/api/messages/id"},
        {"DELETE":"/api/messages/id"},

        
        {"GET":"/api/bookmarks"},
        {"GET":"/api/bookmarks/id"},
        {"PUT":"/api/bookmarks/id"},


        {"GET":"/api/topics"},
        {"POST":"/api/topics"},
        {"GET":"/api/topics/id"},
        {"PUT":"/api/topics/id"},
        {"DELETE":"/api/topics/id"},
        
    ]
    return Response(routes)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def profiles(request):
    profiles = Profile.objects.all()
    if request.method == "GET":
        serializer = ProfileSerializer(profiles, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
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


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comments(request):
    comments = Comment.objects.all()
    if request.method == "GET":
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == "GET":
        serializer = CommentSerializer(comment, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def chats(request):
    chats = Chat.objects.all()
    if request.method == "GET":
        serializer = ChatSerializer(chats, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def chat(request, pk):
    chat = Chat.objects.get(id=pk)

    if request.method == "GET":
        serializer = ChatSerializer(chat, many = False)
        return Response(serializer.data)

    if request.method == "DELETE":
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def messages(request):
    messages = Message.objects.all()
    if request.method == "GET":
        serializer = MessageSerializer(messages, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def message(request, pk):
    message = Message.objects.get(id=pk)

    if request.method == "GET":
        serializer = MessageSerializer(message, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookmarks(request):
    bookmarks = Bookmark.objects.all()
    
    serializer = BookmarkSerializer(bookmarks, many = True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def bookmark(request, pk):
    bookmark = Bookmark.objects.get(id=pk)

    if request.method == "GET":
        serializer = BookmarkSerializer(bookmark, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def topics(request):
    topics = Topic.objects.all()
    if request.method == "GET":
        serializer = TopicSerializer(topics, many = True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def topic(request, pk):
    topic = Topic.objects.get(id=pk)

    if request.method == "GET":
        serializer = TopicSerializer(topic, many = False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

