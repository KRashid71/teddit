from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

## To handle new user creation, writing to database
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'display_name', 'bio']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            display_name=validated_data['password'],
            bio=validated_data.get('bio',''),
        )
        return user
    
## To hanlde User model read operations 
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'bio', 'post_karma', 'comment_karma','date_joined','role']
        read_only_fields = ['post_karma','comment_karma', 'date_joined','role']

