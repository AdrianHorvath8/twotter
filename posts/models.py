from django.db import models
import uuid


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    
