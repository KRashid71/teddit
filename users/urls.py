from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router =DefaultRouter()
router.register('', views.UserViewSet, basename = 'users')

urlpatterns = [
    path('', include(router.urls)),
   # path('register/', views.RegisterView.as_view(), name='register'),
   # path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
]