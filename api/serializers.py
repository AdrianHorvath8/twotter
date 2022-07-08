from rest_framework.serializers import ModelSerializer
from posts.models import Post, Comment
from users.models import Profile, Chat, Message

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"