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
      fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','username','password1')

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

class NeighbourhoodForm(forms.ModelForm):
   '''
   To add new neighbourhood data.
   '''

   class Meta:
      model = Neighbourhood
      fields = ['name','location']

class BusinessForm(forms.ModelForm):
   '''
   To add a new business
   '''

   class Meta:
      model = Business
      fields = ['name','category','email','tel']

class PostForm(forms.ModelForm):
   '''
   To add a post
   '''

   CATEGORIES = (
      ('', 'Select a Category'),
      ('Alert','Alert'),
      ('General','General'),
      ('Announcement','Announcement'),
   )

   content =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What\'s new?'}))
   category = forms.ChoiceField(choices=CATEGORIES,widget=forms.Select())

   class Meta:
      model = Post
      fields = ['content','category']


class AmenitiesForm(forms.ModelForm):
   '''
   To add public amenities.
   '''
   CATEGORIES = (
      ('', 'Select a Category'),
      ('Hospital','Hospital'),
      ('Police','Police'),
      ('Park','Park'),
      ('School','School'),
      ('Fire Department', 'Fire Department')
   )
   amenity_type = forms.ChoiceField(choices=CATEGORIES,widget=forms.Select())
   class Meta:
      model = Amenities
      fields = ['name','tel','email','amenity_type']

class CommentForm(forms.ModelForm):
   '''
   To add comment to post
   '''

   class Meta:
      model = Comment
      fields = ['comment']