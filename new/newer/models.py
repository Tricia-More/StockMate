from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.this is where we create models that we can use for our database for all user info
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-pic.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username 
    
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name