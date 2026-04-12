from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    post_karma = models.IntegerField(default=0)
    comment_karma = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
    