from django.contrib import admin

# Register your models here.

from .models import Profile, Inventory, PerishableInventory

# Register your models here.

admin.site.register(Profile)
admin.site.register(Inventory)
admin.site.register(PerishableInventory)