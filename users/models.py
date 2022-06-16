from django.db import models
import uuid
from django.contrib.auth.models import User



class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.ImageField(null=False, blank=False, upload_to="profiles/", default="profiles/user-default.png")
    email = models.EmailField(max_length=200,null=True, blank=True)
    short_info = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    followers = models.ManyToManyField(User,related_name="followers")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="post", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ["-created"]


    




class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender", null=True, blank=True)
    recipient =  models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipient", null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)
