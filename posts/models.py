

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
    body = models.CharField( max_length=500 ,null=True, blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, blank=True, null=True)
    VOTE_TYPE = (
        ("up", "Up vote"),
        ("down", "Down vote"),
    )
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
    tag = models.ManyToManyField(Tag, blank=True, related_name="tag")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

    class Meta:
        ordering = ["-created"]


