from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Imports needed for registration of users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have  been logged in')
            return redirect('index')
        else:
            messages.error(request, 'Login failed. Incorrect username or password')
            return redirect('login')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successful')
    return redirect('login')


def registerUser(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # login user if registration is successfull
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('index')

        else:
            messages.error(request, 'Whoops! There was a problem registering')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})  # 'form': form passes the form to the webpage


def product(request, id):
    product = Product.objects.get(id=id)

    context = {'product': product}

    return render(request, 'product.html', context)


def category(request, categoryname):
    # categoryname = categoryname.replace('-', ' ')
    try:
        # Finding the category
        category = Category.objects.get(name=categoryname)

        # Getting all the products in that category
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, "That category doesn't exist")
        return redirect('index')
