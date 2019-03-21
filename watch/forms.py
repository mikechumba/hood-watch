from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *


class Registration(UserCreationForm):
   '''
   User registration form.
   '''

   class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','username','password')

class ProfileUpdateForm(forms.ModelForm):
   '''
   To edit user's profile
   '''

   class Meta:
      model = Profile
      fields = ['avatar','neighbourhood']

class LoginForm(AuthenticationForm):
   '''
   To handle user login
   '''

   class Meta:
      model = User
      fields = ['username','password']