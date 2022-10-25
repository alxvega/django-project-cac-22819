from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('index')
        messages.error(request, f'Incorrect password.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')


def signup_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user_info = {
            'username': form.cleaned_data['username'],
            'password': form.cleaned_data['password'],
            'email': form.cleaned_data['email'],

        }
        print(user_info)

    return render(request, 'users/signup.html', {
        'form': RegisterForm()
    })
