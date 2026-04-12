from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    
]