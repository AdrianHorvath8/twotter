from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import Post, Comment, Bookmark, Topic
from users.models import Profile, Chat, Message
from users.views import following
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"





class ProfileSerializer(ModelSerializer):
    
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = Profile
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"


class PostsSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class ChatSerializer(ModelSerializer):
    
    class Meta:
        model = Chat
        fields = "__all__"

class MessageSerializer(ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"


class BookmarkSerializer(ModelSerializer):
    
    class Meta:
        model = Bookmark
        fields = "__all__"


class TopicSerializer(ModelSerializer):
    
    class Meta:
        model = Topic
        fields = "__all__"