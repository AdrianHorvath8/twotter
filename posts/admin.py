from django.contrib import admin
from .models import Post, Comment, Topic


admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)