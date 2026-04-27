from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, ProfileSerializer

User = get_user_model()

# Create your views here.

class UserViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action== 'register':
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]
    
    @action(detail=False, methods=['post'])
    def register(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get', 'patch'], url_path='profile')
    def profile(self, request, pk=None):
        try:
            user = User.objects.get(username=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status = status.HTTP_404_NOT_FOUND
            )
        
        if request.method =='GET':
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        
        if request.user.username !=pk:
            return Response(
                {"error":"You can only update your own profile"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = ProfileSerializer(user, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)