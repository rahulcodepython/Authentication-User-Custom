from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from home.models import Custom_User

import string
import random

# Create your views here.

def index(request):
    return render(request, "index.html")

def login_temp(request):
    return render(request, "login.html")

def login_user(request):
    if request.method=="POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        username = User.objects.get(email=email).username

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    return redirect(profile)

def register_temp(request):
    return render(request, "register.html")

def register_user(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mothername = request.POST.get('mothername')
        fathername = request.POST.get('fathername')
        image = request.FILES['image']
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        dob = request.POST.get('dob')

        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))

        username = firstname + "_" + lastname + "_" + email + "_" + mobile + "_" + str(unique_id)

        # Django build-in user save
        User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password).save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                # Custom User save
                custom_user_id = request.user
                Custom_User(user=custom_user_id, fathername=fathername, mothername=mothername, address=address, dob=dob, mobile=mobile, gender=gender, image=image).save()

                return render(request, "profile.html")

@login_required
def logout_user(request):
    if request.user.is_active:
        logout(request)
    return redirect(login_temp)

def profile(request):
    user = Custom_User.objects.get(user=request.user)

    print(user)

    context = {
        'data': user,
    }

    return render(request, "profile.html", context)

def admin_panel(request):
    user = Custom_User.objects.all()

    context = {
        'datas': user,
    }

    return render(request, "admin.html", context)