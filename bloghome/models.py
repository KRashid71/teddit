from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class AuthorModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    display_handle=models.CharField(max_length=50, unique=True,default='')
    # removed password field as we are using Django's built-in User model for authentication
    #password=models.CharField(max_length=128)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_handle
    
class PostModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=5000)
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    # points=models.IntegerField(default=0)

    @property
    def points(self):
        upvotes=self.postvotemodel_set.filter(vote_type='upvote').count()
        downvotes=self.postvotemodel_set.filter(vote_type='downvote').count()
        return upvotes-downvotes

    def __str__(self):
        return self.title
    
class CommentModel(models.Model):
    post=models.ForeignKey(PostModel, on_delete= models.CASCADE)
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    content=models.TextField(max_length=2000)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author.display_handle} on {self.post.title}'

class VoteModel(models.Model):
 
    VOTE_CHOICES=[('upvote','Upvote'),('downvote','Downvote')]
    vote_type=models.CharField(max_length=10, choices=VOTE_CHOICES)
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class PostVoteModel(VoteModel):
    
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('post', 'author')  # Ensure one vote per author per post

class CommentVoteModel(VoteModel):
    comment=models.ForeignKey(CommentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'author')  # Ensure one vote per author per comment

