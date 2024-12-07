from django.urls import path 
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'), #new url path for the index page
    path('signin', views.signin, name='signin'),
    path('add', views.add, name='add'),
    path('home', views.home, name='home'),
    path('edit', views.edit, name='edit'),
    path('categories', views.categories, name='categories')
]