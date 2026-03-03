from django import forms
from django.contrib.auth.models import User
from .models import AuthorModel, PostModel

class AuthorSignupForm(forms.ModelForm):
    # extra fields for creating the linked User 
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta: 
        model = AuthorModel 
        fields = ['email', 'display_handle', 'username', 'password'] 
        
    def save(self, commit=True): 
    # create the User instance first 
        user = User.objects.create_user( 
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
    # now create the AuthorModel linked to that User 
        author = AuthorModel( 
            user=user,
            email=self.cleaned_data['email'], 
            display_handle=self.cleaned_data['display_handle'] 
        )
        if commit:
            author.save() 
        return author
        
class AuthorSigninForm(forms.Form):
    display_handle=forms.CharField(max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)

class WritePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write some stuff...'}),
        }

