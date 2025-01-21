from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Profile, Inventory, PerishableInventory
from django.contrib.auth.decorators import login_required
#from django.middleware.csrf import get_token

# Create your views here.



def signup(request):
    if request.method == 'POST':
        username = request.POST['username'] #gets the value of the data using th ename pf the input
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect ('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and direct to settings page

                #create a profile oject for the new user 
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
    
def signin(request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None: #if the user is in our db
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'INVALID CREDENTIALS')
                return redirect('signin')
        else:
            return render(request, 'signin.html')

@login_required(login_url='signin')       
def add(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        category = request.POST['category']
        stock = request.POST['stock']
        price = request.POST['price']

         # Check if it's a perishable item
        is_perishable = request.POST.get('is_perishable') == 'on'
        expiration_date = request.POST.get('expiration_date')  # Only if perishable

        if is_perishable:
            # Create a PerishableInventory object and save it
            new_item = PerishableInventory.objects.create(
                item_name=item_name, 
                category=category, 
                stock=stock, 
                price=price, 
                expiration_date=expiration_date
            )
        else:
            # Create a regular Inventory object
            new_item = Inventory.objects.create(
                item_name=item_name, 
                category=category, 
                stock=stock, 
                price=price
            )

        new_item.save()

        return redirect('home')
    else:
        return render(request, 'add.html')


        
            # Create new Inventory object and save to DB
        #new = Inventory.objects.create(item_name=item_name, category=category, stock=stock, price=price)
        #new.save()


@login_required(login_url='signin') 
def home(request):
    
    # Retrieve all products from the Inventory model
    products = Inventory.objects.all()
    #stock_messages = [product.stock_message() for product in products]
        # Iterate through products and call the polymorphic method
    for product in products:
        if isinstance(product, PerishableInventory):
            print(product.stock_message())  # Calls PerishableInventory's method


    # Pass the products to the template
    return render(request, 'home.html', {'products': products},)


@login_required(login_url='signin') 
def edit(request):  # Assuming you are passing the item ID to edit
    # Retrieve the specific item using its ID (or another unique field)
    
    
    if request.method == 'POST':
        # Extract fields from POST data
        item_name = request.POST['item_name']
        category = request.POST['category']
        stock = request.POST['stock']
        price = request.POST['price']

        up = Inventory.objects.update(item_name=item_name, category=category, stock=stock, price=price)
        up.save()

        return HttpResponse("Inventory updated successfully!")
        
            
    return render(request, 'edit.html')
            

@login_required(login_url='signin') 
def categories(request):
    categories = Inventory.objects.values('category').distinct()
    return render(request, 'categories.html', {'categories': categories})






