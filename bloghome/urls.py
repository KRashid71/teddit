from django.urls import path, include
from .views import AuthorSignout, HomeFeed, AuthorSignup, AuthorSignin

urlpatterns = [
    path('', HomeFeed.as_view(), name='homefeed'),
    path('signup/', AuthorSignup.as_view(), name='authorsignup'),
    path('signin/', AuthorSignin.as_view(), name='authorsignin'),
    path('signout/', AuthorSignout.as_view(), name='authorsignout'),
]