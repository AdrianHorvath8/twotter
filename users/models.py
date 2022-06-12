
from django.db import models
import uuid
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    #profile_image = models.ImageField(null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    short_info = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    followers = models.ManyToManyField(User,related_name="followers", null=True, blank=True)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
