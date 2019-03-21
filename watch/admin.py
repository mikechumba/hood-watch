from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Amenities)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)