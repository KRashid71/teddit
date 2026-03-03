from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.db.models import Count, Q
from .models import PostModel, AuthorModel, CommentModel, PostVoteModel
from .forms import AuthorSignupForm, AuthorSigninForm, WritePostForm


# Create your views here.

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            form=WritePostForm()
            posts=PostModel.objects.all().order_by("-created_at")
            # return HttpResponse("Welcome to the Home Page of Teddit!")
            return render(request, "bloghome/home.html",{"form":form,"posts":posts})
        else:
            return redirect('authorsignin')
    
    
    # def post(self, request):
    #     # form= PostForm()
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('home')
    #     posts = PostModel.objects.all().order_by("-created_at")
    #     return render(request, "bloghome/home.html", {"posts": posts})

class WritePostView(View):
    # def get(self,request):
    #     form=WritePostForm()
        # return render(request,'bloghome/write_post.html',{'form':form})
    def post(self,request):
        if request.user.is_authenticated:

            form=WritePostForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.author=request.user.authormodel
                post.save()
                return redirect('home')
        else:
            return redirect('authorsignin')
        # posts=PostModel.objects.all().order_by("-created_at")
        # return render(request,'bloghome/home.html',{'form':form, 'posts': posts})
class AuthorSignup(View):
    def get(self, request):
        form = AuthorSignupForm()
        return render(request, 'bloghome/signup.html', {'form': form})
    
    def post(self, request):
        form = AuthorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorsignin')  # Redirect to signin page after successful signup
        return render(request, 'bloghome/signup.html', {'form': form})
    
class AuthorSignin(View):
    def get(self,request):
        form=AuthorSigninForm()
        return render(request,'bloghome/signin.html',{'form':form})
    
    def post(self,request):
        form=AuthorSigninForm(request.POST)
        if form.is_valid():
            display_handle=form.cleaned_data['display_handle']
            password=form.cleaned_data['password']
            try:
                author=AuthorModel.objects.get(display_handle=display_handle)
                user=authenticate(request, username=author.user.username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')  # Redirect to home page after successful signin
                else:
                    form.add_error(None, 'Invalid credentials')
                    return render(request,'bloghome/signin.html',{'form':form})
            except AuthorModel.DoesNotExist:
                form.add_error('display_handle', 'Author with this display handle does not exist')
                return render(request,'bloghome/signin.html',{'form':form})
        
class AuthorSignout(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('authorsignin')  # Redirect to signin page after signout
        else:
            return redirect('authorsignin')  # Redirect to signin page if not authenticated

class PostListView(View):
    def get(self, request):
        posts= PostModel.objects.all().order_by("-created_at")
        return render(request, "bloghome/post_list.html", {"posts": posts})