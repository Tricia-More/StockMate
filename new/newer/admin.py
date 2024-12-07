from django.contrib import admin

# Register your models here.

from .models import Profile, Inventory

# Register your models here.

admin.site.register(Profile)
admin.site.register(Inventory)