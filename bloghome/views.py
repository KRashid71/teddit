from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Posts
from .forms import AuthorSignupForm 


# Create your views here.

class HomeFeed(View):
    def get(self,request):
        posts=Posts.objects.all().order_by('-time_created')
        
        # return HttpResponse('(posts)')
        return render(request, 'bloghome/home.html', {'posts': posts})
    
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
            return redirect('homefeed')
        return render(request, 'bloghome/signup.html', {'form': form})