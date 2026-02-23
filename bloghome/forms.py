from django import forms
from django.contrib.auth.models import User
from .models import Authors

class AuthorSignupForm(forms.ModelForm):
    
    #fields for user creation
    username = forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Authors
        fields = ['name', 'email', 'display_handle', 'username', 'password']

    def save(self, commit= True):
        #create User instance
        user= User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        #creare author instance linked to User
        author = super().save(commit=False)
        author.user = user
        if commit:
            author.save()
        return author
        