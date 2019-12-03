from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Information


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


def update(request):
    c_user_id = request.user.id
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        bus_name = request.POST['bus_name']
        start_date = request.POST['date']
        currency = request.POST['currency']
        bus_no = request.POST['bus_no']
        alt_bus_no = request.POST['alt_bus_no']
        address = request.POST['address']
        address2 = request.POST['address2']
        website = request.POST['bus_website']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        bus_logo = request.FILES['bus_logo']

        User.objects.filter(id=c_user_id).update(first_name=first_name, last_name=last_name)
        info = Information(user_id=c_user_id, bus_name=bus_name, start_date=start_date,
                           currency=currency, bus_no=bus_no, alt_bus_no=alt_bus_no,
                           address=address, address2=address2, bus_website=website,
                           country=country, city=city, state=state, zip_code=zip_code, bus_logo=bus_logo)
        info.save()
        messages.success(request, 'Updated Successfully')
        return redirect('update')
    else:
        return render(request, 'update.html')
