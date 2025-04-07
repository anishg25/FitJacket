from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CreateUserForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home.index')  # or whatever your homepage is
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('accounts.login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts.login')
