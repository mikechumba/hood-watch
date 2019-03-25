from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='register')
def feed(request):

   hood = request.user.profile.neighbourhood

   title = f'Feed | {hood}'

   posts = Post.objects.filter(hood=hood)
   businesses = Business.objects.filter(hood=hood)
   amenities = Amenities.objects.filter(hood=hood)

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
      'posts': posts,
      'businesses': businesses,
      'amenities': amenities,
      'form': form,
      'hood': hood
   }

   return render(request,'watch/feed.html',context)

@login_required(login_url='register')
def hood_change(request):

   title = f'Change Neighbourhood'

   context = {
      'title': title
   }

   return render(request,'dash/hood_change.html',context)


@login_required(login_url='register')
def new_business(request):

   title = f'Add a New Business in {request.user.profile.neighbourhood}'

   if request.method == 'POST':
      form = BusinessForm(request.POST)
      if form.is_valid():
         business = form.save(commit=False)
         business.owner = request.user.profile
         business.hood = request.user.profile.neighbourhood
         business.save()
         return redirect('feed')
   else:
      form = BusinessForm()

   context =  {
      'form': form,
      'title': title
   }

   return render(request,'watch/new_business.html',context)

def search(request):

   if 'biz_search' in request.GET and request.GET['biz_search']:
      searched = request.GET.get('biz_search')
      if searched:
         businesses = Business.objects.filter(name__icontains=searched).all()
         title = f'Your search {searched} returned'

   context = {
      'businesses': businesses,
      'title': title,
      'searched': searched
   }

   return render(request,'watch/search.html')

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
         return redirect('edit_profile')
   else:
      form = Registration()

   context = {
      'title': title,
      'form': form
   }

   return render(request,'registration/register.html',context)


@login_required(login_url='register')
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

@login_required(login_url='register')
def new_hood(request):

   title = "Add new neighbourhood"

   if request.method == 'POST':
      form = NeighbourhoodForm(request.POST)
      if form.is_valid():
         hood = form.save(commit=False)
         hood.admin = request.user
         hood.save()
         profile = request.user.profile
         profile.neighbourhood = hood
         profile.save()
         return redirect('feed')
   else:
      form = NeighbourhoodForm()

   context = {
      'title': title,
      'form': form
   }

   return render(request,'watch/new_hood.html',context)

@login_required(login_url='register')
def new_amenity(request):

   title = f'Add a New Amenity in {request.user.profile.neighbourhood}'

   if request.method == 'POST':
      form = AmenitiesForm(request.POST)
      if form.is_valid():
         amenity = form.save(commit=False)
         amenity.hood = request.user.profile.neighbourhood
         amenity.save()
         return redirect('feed')
   else:
      form = AmenitiesForm()

   context =  {
      'form': form,
      'title': title
   }

   return render(request,'watch/new_amenity.html',context)

@login_required(login_url='register')
def logout_view(request):
   logout(request)
   return redirect('login')
