

from django.db import models
import uuid




class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    comentator = models.ForeignKey("users.Profile",on_delete=models.CASCADE)
    comment_image = models.ImageField(blank=True, null=True, upload_to="comment/")    
    body = models.TextField(null=True, blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, blank=True, null=True)
    VOTE_TYPE = (
        ("up", "Up vote"),
        ("down", "Down vote"),
    )
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.comentator)

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.ForeignKey("users.Profile", on_delete=models.SET_NULL, related_name="owner" , null=True, blank=True)
    post_image = models.ImageField(blank=True, null=True, upload_to="post/")    
    body = models.TextField(null=True, blank=True)
    VOTE_TYPE = (
        ("up", "Up vote"),
        ("down", "Down vote"),
    )
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)


