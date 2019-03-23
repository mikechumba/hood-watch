from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .models import *
from .forms import *

# Create your views here.
def landing(request):

   return render(request,'watch/landing.html')


def feed(request):

   hood = request.user.profile.neighbourhood

   title = f'Feed | {hood}'

   posts = Post.objects.filter(hood=request.user.profile.neighbourhood).all()

   context = {
      'title': title,
      'posts': posts
   }

   return render(request,'watch/feed.html',context)

def dashboard(request):

   title = f'Dashboard'

   context = {
      'title': title
   }

   return render(request,'watch/dashboard.html',context)

def hood_change(request):

   title = f'Change Neighbourhood'

   context = {
      'title': title
   }

   return render(request,'dash/hood_change.html',context)

def new_post(request):

   hood = request.user.profile.neighbourhood

   title = f"New Post in {hood}"

   if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user.profile
         post.hood = request.user.profile.neighbourhood
         post.save()
         return redirect('feed')
   else:
      form = PostForm()
   
   context = {
      'title': title,
      'form': form,
   }

   return render(request,'watch/new_post.html',context)

def register(request):

   title = 'Sign Up'

   if request.method == 'POST':
      form = Registration(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password')
         user = authenticate(username=username,password=raw_password)
         login(request,user)
         profile = Profile(user=user)
         profile.save()
         return redirect('landing')
   else:
      form = Registration()

   context = {
      'title': title,
      'form': form
   }

   return render(request,'registration/register.html',context)

def edit_profile(request):

   title = 'Edit Profile'

   user = request.user

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
      if form.is_valid():
         form.save()
         return redirect('profile')
   else:
      form = ProfileUpdateForm(instance=user.profile)

   context = {
      'title': title,
      'form': form
   }

   return render(request,'dash/edit_profile.html',context)


def profile(request):

   user = request.user

   title = f'{user.first_name} {user.last_name}'

   context = {
      'title': title
   }

   return render(request,'watch/profile.html',context)


def logout_view(request):
   logout(request)
   return redirect('login')