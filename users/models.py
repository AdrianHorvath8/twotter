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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ["-created"]


    
class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    chat_member_one = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    chat_member_two =  models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="chat_member_two", null=True, blank=True)
    

class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=10000 ,null=True, blank=True)
    message_image = models.ImageField(null=True, blank=True, upload_to="message/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)
    
    class Meta:
        ordering = ["-created"]



