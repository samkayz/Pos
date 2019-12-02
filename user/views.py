from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                user.save()
                messages.success(request, 'Registration Successful')
                return redirect('signup')
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
