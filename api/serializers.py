from rest_framework.serializers import ModelSerializer
from posts.models import Post, Comment
from users.models import Profile, Chat, Message
from users.views import following
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




class ProfileSerializer(ModelSerializer):
    following = UserSerializer(many=True)
    followers = UserSerializer(many=True)
    class Meta:
        model = Profile
        fields = "__all__"

class PostsSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"