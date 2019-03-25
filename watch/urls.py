from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
   path('', views.feed,name='feed'),
   path('register/',views.register,name='register'),
   path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,extra_context={'title': 'Login'}),name='login'),
   path('logout/',views.logout_view,name='logout'),
   path('neighbourhood/new',views.new_hood,name='new_hood'),
   path('amenity/new',views.new_amenity,name='new_amenity'),
   path('profile/edit',views.edit_profile,name='edit_profile'),
   path('search/',views.search,name='search'),
   path('business/new',views.new_business,name='new_business')
]