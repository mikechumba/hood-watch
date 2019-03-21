from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
   '''
   Hold location data
   '''
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

class Neighbourhood(models.Model):
   '''
   Holds neighbourhood data
   '''

   name = models.CharField(max_length=50)
   location = models.ForeignKey(Location, on_delete=models.CASCADE)
   admin = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatars/',default='default.jpg')
   neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

   def __str__(self):
      return self.user.username

class Category(models.Model):
   '''
   Hold business categories
   '''

   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Categories"

class Business(models.Model):
   '''
   Holds info on businesses in each neighbourhood
   '''

   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   owner = models.ForeignKey(Profile,on_delete=models.CASCADE)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Businesses"

class Amenities(models.Model):
   '''
   To hold data on a neighbourhood's public amenities
   '''

   name = models.CharField(max_length=50)
   tel = models.IntegerField()
   email = models.EmailField(max_length=254)
   amenity_type = models.CharField(max_length=50)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = 'Amenities'

class Post(models.Model):
   '''
   Hold post data.
   '''

   content = models.CharField(max_length=280)
   # category = models.ForeignKey(Category, on_delete=models.CASCADE)
   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
   category = models.CharField(max_length=50,default='General')

   def __str__(self):
      return self.content

class Comment(models.Model):
   '''
   Hold post comment data
   '''

   comment = models.CharField(max_length=50)
   comment_on = models.ForeignKey(Post, on_delete=models.CASCADE)
   comment_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

   def __str__(self):
      return self.comment