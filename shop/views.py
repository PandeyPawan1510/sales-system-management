from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            
            d={"message":"invalid password thkur"}
            return render(request,"login.html",d)
    else:
        return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
def buy (request):

    return render(request,"buy.html")

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


from django.shortcuts import render, redirect
from .models import Order

def check(request):
    orders = Order.objects.filter(client=request.user)  # Assuming user is authenticated and each order is associated with a client
    total = sum(order.total_price for order in orders)
    return render(request, 'check.html', {'orders': orders, 'total': total})

def confirm_order(request):
    # Logic to confirm the order
    # For example: mark orders as confirmed, clear the cart, etc.
    # After processing, redirect the user to a thank you page or back to the product list
    return redirect('product')


 
    
    
