from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .UserForms import SignUpForm

def signup(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            messages.success(request, ("Account Created Successfully."))
            return redirect('login') 
        else:
            print("Not Valid")
            print(form.errors)
            messages.error(request, (form.errors))
            return redirect('signup') 
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful.")
            return redirect('/')  # Redirect to products or any other page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')  # Redirect to login page after logout