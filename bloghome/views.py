from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Posts, Authors, Comment
from .forms import AuthorSignupForm, AuthorSigninForm 


# Create your views here.

class HomeFeed(View):
    def get(self,request):
        posts=Posts.objects.all().order_by('-time_created')
        
        # return HttpResponse('(posts)')
        return render(request, 'bloghome/home.html', {'posts': posts})
    
    def post(self,request):
        if request.user.is_authenticated:
            post_id = request.POST.get('post_id')
            content = request.POST.get('content')
            if post_id and content:
                post = get_object_or_404(Posts, id=post_id)
                Comment.objects.create(
                    post=post,
                    author=request.user.authors,
                    content=content
                )
        return redirect('homefeed')

class AuthorSignup(View):
    # to render empty signup form
    def get(self,request):
        form = AuthorSignupForm()
        return render(request, 'bloghome/signup.html', {'form': form})
    
    # to process form submission data
    def post(self,request):
        form = AuthorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorsignin')
        return render(request, 'bloghome/signup.html', {'form': form})
    
class AuthorSignin(View):
    def get(self,request):
        form = AuthorSigninForm()
        return render(request, 'bloghome/signin.html', {'form': form})
    
    def post(self,request):
        form= AuthorSigninForm(request.POST)
        if form.is_valid():
            display_handle=form.cleaned_data['display_handle']
            password=form.cleaned_data['password']

            try:
                #fetch author with matching display_handle
                author = Authors.objects.get(display_handle=display_handle)
                user = author.user
            except Authors.DoesNotExist:
                form.add_error('display_handle', 'Invalid display handle')
                return render(request,'bloghome/signin.html',{'form': form})
            
            #Authenticate user using Django's authentication system
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request,user)
                return redirect('homefeed')
            else:
                form.add_error(password, 'Invalid password')

        return render(request,'bloghome/signin.html',{'form': form})
    
class AuthorSignout(View):

    def get(self, request):
        logout(request)
        return redirect('authorsignin')