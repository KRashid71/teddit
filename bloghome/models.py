from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Authors(models.Model):
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE)
    #user=models.OneToOneField(User, on_delete=models.CASCADE)
    #--worked first--->user=models.OneToOneField(User, on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    display_handle=models.CharField(max_length=50, unique=True, default='')
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Posts(models.Model):
    author=models.ForeignKey('Authors', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Authors(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     display_handle=models.CharField(max_length=50, unique=True, default='')
#     password = models.CharField(max_length=100)
#     date_joined = models.DateTimeField(default=timezone.now)


    

    

