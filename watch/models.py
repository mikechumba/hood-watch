from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
   '''
   Holds neighbourhood data
   '''

   name = models.CharField(max_length=50)
   location = models.CharField(max_length=50)
   admin = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

class Profile(models.Model):
   '''
   Holds user's profile data.
   '''


   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatars/')
   neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

   def __str__(self):
      return self.user.username


class Business(models.Model):
   '''
   Holds info on businesses in each neighbourhood
   '''

   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
   category = models.ForeignKey(Category,)

   def __str__(self):
      return self.name

class HealthCenter(models.Model):
   '''

   '''
