

from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    comentator = models.ForeignKey("users.Profile",on_delete=models.CASCADE)
    comment_image = models.ImageField(blank=True, null=True, upload_to="comment/")    
    body = models.CharField( max_length=500 ,null=True, blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, blank=True, null=True)
    like = models.ManyToManyField("users.Profile", blank=True, related_name="like")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.body)

    class Meta:
        ordering = ["-created"]



class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.ForeignKey("users.Profile", on_delete=models.SET_NULL, related_name="owner" , null=True, blank=True)
    post_image = models.ImageField(blank=True, null=True, upload_to="post/")    
    body = models.CharField(max_length=500 ,null=True, blank=True)
    like = models.ManyToManyField("users.Profile", blank=True, related_name="likes")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

    class Meta:
        ordering = ["-created"]


class Topic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    body = models.CharField( max_length=100 ,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

    class Meta:
        ordering = ["?"]


class Bookmark(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    profile = models.OneToOneField("users.Profile", on_delete=models.CASCADE, null=True, blank=True)
    post = models.ManyToManyField(Post, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)