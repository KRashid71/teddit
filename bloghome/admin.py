from django.contrib import admin
from .models import PostModel, AuthorModel, CommentModel, PostVoteModel, CommentVoteModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(AuthorModel)
admin.site.register(CommentModel)
admin.site.register(PostVoteModel)
admin.site.register(CommentVoteModel)