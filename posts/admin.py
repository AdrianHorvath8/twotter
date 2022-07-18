from django.contrib import admin
from .models import Post, Comment, Topic, Bookmark


admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Bookmark)