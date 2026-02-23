from django.urls import path, include
from .views import HomeFeed, AuthorSignup

urlpatterns = [
    path('', HomeFeed.as_view(), name='homefeed'),
    path('signup/', AuthorSignup.as_view(), name='authorsignup'),

]