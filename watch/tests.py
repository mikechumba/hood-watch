from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
def create_user_instance():
   user = User(username='johndoe', first_name='John', last_name='Doe', password='password')
   return user

def create_profile_instance(user,hood):
   profile = Profile(user=user,avatar='default.jpg',neighbourhood=hood)
   return profile

def create_hood_instance(lctn,user):
   hood = Neighbourhood(name='Bel Air',location=lctn,admin=user)
   return hood

def create_category_instance():
   category = Category(name='This is category')
   return category

def create_business_instance(hood,ctgry,prfl):
   business = Business(name='A Biz',email='biz@email.com',tel=25495034,hood_id=1,category_id=1,owner_id=1)
   return business

def create_amenity_instance(hood):
   amenity = Amenities(name='Amenity',tel='247493494',email='amenity@email.com',amenity_type='Just an Amenity',hood=hood)
   return amenity

def create_post_instance(prfl,hood):
   post = Post(content='This is a post',author=prfl,hood=hood,category='A category')
   return post

def create_location_instance():
   location = Location(name='A Location')
   return location

class UserTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()

   def test_user_instance(self):
      self.assertTrue(isinstance(self.new_user,User))

   def test_save_user(self):
      self.new_user.save()
      users = User.objects.all()
      self.assertTrue(len(users),1)

class ProfileTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_location = create_location_instance()
      self.new_location.save()
      self.new_hood = create_hood_instance(self.new_location,self.new_user)
      self.new_hood.save()
      self.new_profile = create_profile_instance(self.new_user,self.new_hood)

   def test_profile_instance(self):
      self.assertTrue(isinstance(self.new_profile,Profile))

   def test_save_profile(self):
      self.new_profile.save()
      profiles = Profile.objects.all()
      self.assertTrue(len(profiles),1)

class HoodTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_location = create_location_instance()
      self.new_location.save()
      self.new_hood = create_hood_instance(self.new_location,self.new_user)

   def test_hood_instance(self):
      self.assertTrue(isinstance(self.new_hood,Neighbourhood))

   def test_create_neighbourhood(self):
      self.new_hood.create_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertTrue(len(hoods),1)

   def test_find_neighbourhood(self):
      self.new_hood.save()
      hood = Neighbourhood.find_neighbourhood(self.new_hood.pk)
      self.assertEqual(hood,self.new_hood)

   def test_update_neighbourhood(self):
      self.new_hood.save()
      self.new_hood.name = 'Hollywood'
      self.new_hood.update_neighbourhood()
      self.assertEqual(self.new_hood.name,'Hollywood')

   def test_update_occupants(self):
      self.new_hood.save()
      occupants = Neighbourhood.update_occupants(self.new_hood.pk)
      self.new_user.save()
      occupants = create_profile_instance(self.new_user,self.new_hood)
      occupants.save()
      profiles = Profile.objects.all()
      new_occupants = Neighbourhood.update_occupants(self.new_hood.pk)
      self.assertEqual(len(profiles),1)

   def test_delete_instance(self):
      self.new_hood.save()
      self.new_hood.delete_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertEqual(len(hoods),0)


class Business(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_location = create_location_instance()
      self.new_location.save()
      self.new_hood = create_hood_instance(self.new_location,self.new_user)
      self.new_hood.save()
      self.new_profile = create_profile_instance(self.new_user,self.new_hood)
      self.new_profile.save()
      self.new_category = create_category_instance()
      self.new_category.save()
      self.new_business = create_business_instance(self.new_hood,self.new_category,self.new_profile)

   # def test_business_instance(self):
   #    self.assertTrue(isinstance(self.new_business,Business))

   # def test_save_business(self):
   #    self.new_business.save()
   #    businesses = Business.objects.all()
   #    self.assertTrue(len(businesses),1)


class AmenityTest(TestCase):

   def setUp(self):
      
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_location = create_location_instance()
      self.new_location.save()
      self.new_hood = create_hood_instance(self.new_location,self.new_user)
      self.new_hood.save()
      self.new_amenity = create_amenity_instance(self.new_hood)

   def test_amenity_instance(self):
      self.assertTrue(isinstance(self.new_amenity,Amenities))

   
   def test_save_amenity(self):
      self.new_amenity.save()
      amenities = Amenities.objects.all()
      self.assertTrue(len(amenities),1)


class PostTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_location = create_location_instance()
      self.new_location.save()
      self.new_hood = create_hood_instance(self.new_location,self.new_user)
      self.new_hood.save()
      self.new_profile = create_profile_instance(self.new_user,self.new_hood)
      self.new_profile.save()
      self.new_post = create_post_instance(self.new_profile,self.new_hood)

   def test_post_instance(self):
      self.assertTrue(isinstance(self.new_post,Post))


   def test_save_post(self):
      self.new_post.save()
      posts = Post.objects.all()
      self.assertTrue(len(posts),1)
