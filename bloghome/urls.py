from django.urls import path, include
from .views import Home, AuthorSignup, AuthorSignin, AuthorSignout, WritePostView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', AuthorSignup.as_view(), name='authorsignup'),
    # # path('', AuthorSignup.as_view(), name='authorsignup'),
    path('signin/', AuthorSignin.as_view(), name='authorsignin'),
    path('signout/', AuthorSignout.as_view(), name='authorsignout'),
    path('writepost/', WritePostView.as_view(), name='write_post'),
]