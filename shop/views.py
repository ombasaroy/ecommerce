from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
