from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from .models import *
from .forms import *

# Create your views here.
def landing(request):

   return render(request, 'watch/landing.html')

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

   return render(request, 'registration/register.html')