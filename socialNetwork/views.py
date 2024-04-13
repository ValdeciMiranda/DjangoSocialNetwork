from django.shortcuts import render, redirect
from .forms import RegisterNewUserForm, UserLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request, 'index.html')


def register(request):

    form = RegisterNewUserForm()

    if request.method == "POST":
        form = RegisterNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'registerform': form}

    return render(request, 'register.html', context=context)


def login(request):

    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:

                auth.login(request, user)
                return redirect('feed')

    context = {'loginform': form}

    return render(request, 'login.html', context=context)

def LogoutUser(request):

    auth.logout(request)

    return redirect("")

@login_required(login_url='login')
def feed(request):

    return render(request, 'feed.html')

